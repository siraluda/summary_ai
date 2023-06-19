from transformers import pipeline
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from .constants import WELCOME_MESSAGE

#initialize Fastapi application
app = FastAPI()

#download transformer model from huggingface
summerizer = pipeline("summarization", model="facebook/bart-large-cnn")


class TextData(BaseModel):
    title: str
    text: str
    min_length: Optional[int] = 50
    max_length: Optional[int] = 150


@app.get("/")
def home():
    return {"app_description": WELCOME_MESSAGE}


@app.post("/summarize")
def summarize(text_data: TextData):
    result = summerizer(
        text_data.text,
        max_length=text_data.max_length,
        min_length=text_data.min_length,
        do_sample=False,
    )
    summary = result[0]
    summary["title"] = text_data.title
    return summary
