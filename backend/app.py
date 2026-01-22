from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model import SimpleLLM, SimpleTokenizer

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize
model = SimpleLLM()
tokenizer = SimpleTokenizer()


class GenerateRequest(BaseModel):
    prompt: str
    max_length: int = 20
    temperature: float = 0.7


class GenerateResponse(BaseModel):
    prompt: str
    generated_text: str
    full_text: str


@app.get("/")
def root():
    return {"message": "Simple LLM API is running!"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/generate")
def generate(request: GenerateRequest):
    try:
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
