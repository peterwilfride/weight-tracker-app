from fastapi import FastAPI
from src.models.weight_model import WeightModel
from src.services.weight_service import WeightService

app = FastAPI()

weight_service = WeightService()

@app.get("/weights", status_code=200)
async def list_weightss():
    return weight_service.list_all()

@app.post("/weights", status_code=201)
async def register_weight(weight: WeightModel):
    weight_service.register(weight)
    return {'response': 'Saved sucessfully'}