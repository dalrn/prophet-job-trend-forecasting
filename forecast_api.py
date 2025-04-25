from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
from prophet.serialize import model_from_json
import json, re

app = FastAPI()

def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|, ]+', '_', name)

class InputData(BaseModel):
    # terima input category dan list dates dari user
    category: str
    dates: list[str]

@app.post("/predict")
def predict(data: InputData):
    try:
        # ubah date jadi tipe format datetime
        df_future = pd.DataFrame({'ds': pd.to_datetime(data.dates)})
        
        # load model prediksi yang sesuai category yang diinput user
        filename = f"models/prophet_model_{sanitize_filename(data.category)}.json"
        with open(filename, "r") as f:
            model = model_from_json(json.load(f))
        
        # predict 
        forecast = model.predict(df_future)
        results = forecast[['ds', 'yhat']].to_dict(orient="records")
        return {"predictions": results}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
