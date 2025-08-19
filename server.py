from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow requests from your browser
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/submit")
async def submit(request: Request):
    data = await request.json()
    print("Received:", data)  # logs to your terminal
    return {"received": data}
