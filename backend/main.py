from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline,TFBertForTokenClassification
from model import LanguageModel

class TextRequest(BaseModel):
    text: str

app = FastAPI()


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3001",
    "http://localhost:3002",
    "http://localhost:3003",
    "http://localhost:3004",
    "http://localhost:3000",
    "http://localhost:8080",
    "http://127.0.0.1:8000/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ner")
async def ner_response(textRequest: TextRequest):
    #print("inside with item", textRequest)
    languageModel = LanguageModel(pipeline('ner', model='KB/bert-base-swedish-cased-ner', tokenizer='KB/bert-base-swedish-cased-ner', ignore_labels=[]))
    response = languageModel.named_entity_recognition(textRequest.text)
    print(response)

    return {
        "text": response }

