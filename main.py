# from fastapi import FastAPI, Request
# from pydantic import BaseModel

# app = FastAPI()

# # Data model for POST request
# class DataModel(BaseModel):
#     message: str

# # GET method to return a string message sent from C# Unity
# @app.get("/get-message")
# async def get_message():
#     # Example of a response that Unity can call and print
#     return {"message": "Hello from FastAPI!"}

# # POST method to receive a message from C# Unity and print it in the backend
# @app.post("/post-message")
# async def post_message(data: DataModel):
#     print(f"Received message from Unity: {data.message}")
#     # Response that will be sent back to Unity
#     return {"message": "Message received by FastAPI!"}

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for communication between FastAPI and React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this for production (e.g., specific frontend domain)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the request body
class MessageRequest(BaseModel):
    message: str

# Route to receive the message and send back the response
@app.post("/reply")
async def reply_to_message(request: MessageRequest):
    # You can process the message or do any logic here
    return {"response": "Oh ok, that's a nice one."}
