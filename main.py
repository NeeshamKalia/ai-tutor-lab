from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from ollama import AsyncClient

app = FastAPI(
    title="AI Tutor Lab",
    description="Backend API for AI Tutor Lab",
    version="0.1.0"
)

@app.get("/")
async def root():
    return {"message": "Welcome to AI Tutor Lab API's!!"}

#sdrfdsfds
@app.get("/health-check")
async def health_check():
    return {"status": "of89k"}

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_with_model(request: ChatRequest):
    async def generate_response():
        # Call ollama with stream=True
        async for chunk in await AsyncClient().chat(
            model='gemma4:e4b',
            messages=[{'role': 'user', 'content': request.message}],
            stream=True
        ):
            # Extract the content from the chunk and yield it
            content = chunk['message']['content']
            if content:
                yield content

    return StreamingResponse(generate_response(), media_type="text/plain")