from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

LAMBDA_URL = "https://<api-gateway-url>.execute-api.<region>.amazonaws.com/prod/process"

@app.post("/process-data/")
async def process_data(data: dict):
    try:
        response = requests.post(LAMBDA_URL, json=data)
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error processing data")
