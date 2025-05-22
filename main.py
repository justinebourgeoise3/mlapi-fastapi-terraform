from fastapi import FastAPI
from pydantic import BaseModel
from app.model import predict

app = FastAPI()

class InputData(BaseModel):
    text: str

@app.post("/predict")
def get_prediction(data: InputData):
    result = predict(data.text)
    return {"prediction": result}
