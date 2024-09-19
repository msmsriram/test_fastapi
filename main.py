from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

# Data model for POST request
class DataModel(BaseModel):
    message: str

# GET method to return a string message sent from C# Unity
@app.get("/get-message")
async def get_message():
    # Example of a response that Unity can call and print
    return {"message": "Hello from FastAPI!"}

# POST method to receive a message from C# Unity and print it in the backend
@app.post("/post-message")
async def post_message(data: DataModel):
    print(f"Received message from Unity: {data.message}")
    # Response that will be sent back to Unity
    return {"message": "Message received by FastAPI!"}
