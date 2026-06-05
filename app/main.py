import os

from dotenv import load_dotenv
from fastapi import FastAPI
from groq import Groq
from pydantic import BaseModel

load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY")) 

app=FastAPI(
    title="Code Review Buddy",
    description="AI-powered Python code reviewer"

)



class ReviewRequest(BaseModel):
    code:str

class ReviewResponse(BaseModel):
    review:str

@app.get("/health")
def health_check():
    return {
        "status":"healthy",
        "message": "Code Review Buddy is running"

    }

@app.post("/review_input",response_model=ReviewResponse)
def review_code(request:ReviewRequest):

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role":"system",
                "content":"Hi! Upload the code for a review "
            },
            {
                "role": "user",
                "content": f"Check this code: {request.code}"
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    return ReviewResponse(review=chat_completion.choices[0].message.content)






