import torch
import torch.nn as nn
from collections import defaultdict


class SimpleTokenizer:
    """Convert text to numbers and back"""
    def __init__(self):
        self.vocab = defaultdict(int)
        self.vocab["<PAD>"] = 0
        self.vocab["<UNK>"] = 1

    def fit(self, texts):
        for text in texts:
            for word in text.split():
                if word not in self.vocab:
                    self.vocab[word] = len(self.vocab)

    def encode(self, text):
        return [self.vocab.get(word, self.vocab["<UNK>"]) for word in text.split()]

    def decode(self, tokens):
        reverse_vocab = {v: k for k, v in self.vocab.items()}
        return " ".join([reverse_vocab.get(token, "<UNK>") for token in tokens])


class EmbeddingLayer(nn.Module):
    """Convert token IDs to embeddings"""
    def __init__(self, vocab_size, embed_dim):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)

    def forward(self, x):
        return self.embedding(x)


class SelfAttention(nn.Module):
    """Self-attention mechanism"""
    def __init__(self, embed_dim):
        super().__init__()
        self.query = nn.Linear(embed_dim, embed_dim)
        self.key = nn.Linear(embed_dim, embed_dim)
        self.value = nn.Linear(embed_dim, embed_dim)

    def forward(self, x):
        Q = self.query(x)
        K = self.key(x)
        V = self.value(x)
        scores = torch.matmul(Q, K.transpose(-2, -1)) / (x.size(-1) ** 0.5)
        weights = torch.softmax(scores, dim=-1)
        output = torch.matmul(weights, V)
        return output


class TransformerBlock(nn.Module):
    """Transformer block with attention and feed-forward"""
    def __init__(self, embed_dim):
        super().__init__()
        self.attention = SelfAttention(embed_dim)
        self.feed_forward = nn.Sequential(
            nn.Linear(embed_dim, embed_dim * 4),
            nn.ReLU(),
            nn.Linear(embed_dim * 4, embed_dim)
        )
        self.norm1 = nn.LayerNorm(embed_dim)
        self.norm2 = nn.LayerNorm(embed_dim)

    def forward(self, x):
        x = x + self.attention(self.norm1(x))
        x = x + self.feed_forward(self.norm2(x))
        return x


class SimpleLLM(nn.Module):
    """Simple transformer-based language model"""
    def __init__(self, vocab_size, embed_dim, num_blocks):
        super().__init__()
        self.embedding = EmbeddingLayer(vocab_size, embed_dim)
        self.blocks = nn.ModuleList([TransformerBlock(embed_dim) for _ in range(num_blocks)])
        self.fc = nn.Linear(embed_dim, vocab_size)

    def forward(self, x):
        x = self.embedding(x)
        for block in self.blocks:
            x = block(x)
        logits = self.fc(x)
        return logits
