from fastapi import FastAPI
from PIL import Image
import io
from fastapi.responses import FileResponse
from transformers import ViltProcessor, ViltForQuestionAnswering
from PIL import Image
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request
from pydantic import BaseModel
from typing import Any
from starlette.requests import Request



processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")


class QuestionRequest(BaseModel):
    text: str
    image: Any 


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

def model_pipeline(text :str, image : Image):
    
    encoding = processor(image, text, return_tensors="pt")
    outputs = model(**encoding)
    logits = outputs.logits
    idx = logits.argmax(-1).item()

    return  model.config.id2label[idx]


@app.get("/")
def read_root():

    return FileResponse("static/index.html")

@app.post("/ask")
async def ask(request: Request):
    form_data = await request.form()
    request_data = QuestionRequest(
        text=form_data.get("question", ""),
        image=await form_data.get("image").read(),
    )

    image = Image.open(io.BytesIO(request_data.image))
    result = model_pipeline(request_data.text, image)
    return {"answer": result}


