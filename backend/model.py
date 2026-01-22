class SimpleLLM:
    """Ultra-lightweight text generator"""
    def __init__(self):
        self.responses = {
            "cat": "The cat is cute and furry",
            "dog": "The dog is loyal and friendly",
            "bird": "The bird can fly high in the sky",
            "sun": "The sun rises in the morning",
            "apple": "Apples are sweet and healthy",
            "coffee": "Coffee is hot and energizing",
            "the": "The weather is beautiful today"
        }
    
    def generate(self, prompt, max_length=20, temperature=0.7):
        """Generate response"""
        words = prompt.lower().split()
        
        # Find if any keyword in prompt
        for word in words:
            if word in self.responses:
                return self.responses[word]
        
        # Default response
        return "That's an interesting topic. Tell me more about it."


class SimpleTokenizer:
    """Minimal tokenizer"""
    def __init__(self):
        self.vocab = {}
    
    def fit(self, texts):
        pass
    
    def encode(self, text):
        return text.split()
    
    def decode(self, tokens):
        return " ".join(str(t) for t in tokens)

