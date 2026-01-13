from fastapi import FastAPI
from pydantic import BaseModel
from ai_agent import process_message

app = FastAPI()

class Message(BaseModel):
    text: str

@app.post("/ai")
def ai_endpoint(msg: Message):
    response = process_message(msg.text)
    return {"response": response}
