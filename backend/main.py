import httpx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
import json

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    model: str = "llama3"
    messages: List[Dict[str, str]]
    stream: bool = True

from fastapi.responses import StreamingResponse

@app.post("/chat")
async def chat(request: ChatRequest):
    ollama_url = "http://localhost:11434/api/chat"
    
    async def generate():
        try:
            async with httpx.AsyncClient() as client:
                # Forward the request to Ollama
                async with client.stream("POST", ollama_url, json=request.dict(), timeout=None) as response:
                    if response.status_code != 200:
                        yield json.dumps({"error": "Ollama API error"}).encode()
                        return
                    
                    async for chunk in response.aiter_bytes():
                        yield chunk
                        
        except httpx.RequestError as exc:
             yield json.dumps({"error": f"An error occurred while requesting {exc.request.url!r}."}).encode()

    return StreamingResponse(generate(), media_type="application/x-ndjson")

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/models")
async def get_models():
    """Fetch available Ollama models"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("http://localhost:11434/api/tags")
            response.raise_for_status()
            data = response.json()
            models = [model["model"] for model in data.get("models", [])]
            return {"models": models}
    except httpx.ConnectError:
        raise HTTPException(
            status_code=503,
            detail="Could not connect to Ollama server. Please ensure Ollama is running."
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
