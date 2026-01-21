import random
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


class SimpleLLM:
    """Simple LLM without PyTorch (lightweight for deployment)"""
    def __init__(self, vocab_size, embed_dim=16, num_blocks=2):
        self.vocab_size = vocab_size
        self.embed_dim = embed_dim
        self.num_blocks = num_blocks
        # Simple word co-occurrence matrix for lightweight inference
        self.word_pairs = defaultdict(list)
    
    def train(self, texts, tokenizer):
        """Learn word patterns from training texts"""
        for text in texts:
            words = text.split()
            for i in range(len(words) - 1):
                self.word_pairs[words[i]].append(words[i + 1])
    
    def predict_next(self, word):
        """Predict next word based on learned patterns"""
        if word in self.word_pairs and self.word_pairs[word]:
            return random.choice(self.word_pairs[word])
        # Fallback words
        common_words = ["the", "a", "and", "cat", "dog", "sat", "mat", "on", "is", "was"]
        return random.choice(common_words)
    
    def generate(self, prompt, max_length=20, temperature=0.7):
        """Generate text"""
        words = prompt.split()
        
        for _ in range(max_length):
            if not words:
                break
            
            # Get last word and predict next
            current_word = words[-1].strip('.,!?')
            next_word = self.predict_next(current_word.lower())
            
            # Apply temperature (randomness)
            if random.random() > temperature:
                # Sometimes pick random word instead
                common = ["the", "a", "and", "is", "was", "in", "on", "at", "to", "of"]
                next_word = random.choice(common)
            
            words.append(next_word)
        
        return " ".join(words[len(prompt.split()):])

