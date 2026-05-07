from fastapi import FastAPI

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