from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model import SimpleLLM, SimpleTokenizer

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global model and tokenizer
model = None
tokenizer = None


def init_model():
    """Initialize model and tokenizer"""
    global model, tokenizer
    
    # Training data
    texts = [
        "The cat sat on the mat",
        "The dog barked at the cat",
        "A bird flew over the house",
        "The sun rises in the east",
        "Apples and bananas are fruits",
        "She drinks coffee every morning",
        "The weather is nice today",
        "I love programming in Python",
        "Cats are very cute animals",
        "Dogs are loyal companions",
    ]
    
    # Initialize tokenizer
    tokenizer = SimpleTokenizer()
    tokenizer.fit(texts)
    vocab_size = len(tokenizer.vocab)
    
    # Initialize model
    model = SimpleLLM(vocab_size=vocab_size, embed_dim=16, num_blocks=2)
    # Train the model
    model.train(texts, tokenizer)


# Request/Response models
class GenerateRequest(BaseModel):
    prompt: str
    max_length: int = 20
    temperature: float = 0.7


class GenerateResponse(BaseModel):
    prompt: str
    generated_text: str
    full_text: str


@app.on_event("startup")
async def startup_event():
    """Initialize model on startup"""
    init_model()


@app.get("/")
async def root():
    return {"message": "Simple LLM API is running!"}


@app.get("/health")
async def health():
    return {"status": "healthy"}


@app.post("/generate", response_model=GenerateResponse)
async def generate(request: GenerateRequest):
    """Generate text based on prompt"""
    try:
        # Generate text
        generated_text = model.generate(
            request.prompt,
            max_length=request.max_length,
            temperature=request.temperature
        )
        
        full_text = request.prompt + " " + generated_text
        
        return GenerateResponse(
            prompt=request.prompt,
            generated_text=generated_text,
            full_text=full_text
        )
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
