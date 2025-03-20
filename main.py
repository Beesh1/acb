from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

HF_API_TOKEN = os.getenv("HF_API_TOKEN")
HF_API_URL = "https://api-inference.huggingface.co/models/bigcode/starcoder"

def get_ai_suggestion(code_input: str) -> str:
    if not HF_API_TOKEN:
        return "Error: HF_API_TOKEN not set in .env"
    headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}
    payload = {
        "inputs": f"Code: {code_input}\nSuggestion: ",
        "parameters": {"max_new_tokens": 50, "temperature": 0.7}
    }
    try:
        response = requests.post(HF_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()[0]["generated_text"]
        return result.split("Suggestion: ")[-1].strip()
    except Exception as e:
        return f"AI error: {str(e)}"

@app.get("/")
async def get():
    return HTMLResponse("<h1>AI Code Buddy Lives!</h1>")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        ai_response = get_ai_suggestion(data)
        await websocket.send_text(f"AI: {ai_response}")