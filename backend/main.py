from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

app = FastAPI()

ALERT_FILE = "data/alerts.json"


class Alert(BaseModel):
    source: str
    severity: str
    event: str
    ip: str


@app.get("/")
def home():
    return {"message": "CyberGuard AI Running"}


@app.post("/alert")
def create_alert(alert: Alert):

    os.makedirs("data", exist_ok=True)

    if not os.path.exists(ALERT_FILE):
        with open(ALERT_FILE, "w") as f:
            json.dump([], f)

    try:
        with open(ALERT_FILE, "r") as f:
            alerts = json.load(f)
    except:
        alerts = []

    alerts.append(alert.model_dump())

    with open(ALERT_FILE, "w") as f:
        json.dump(alerts, f, indent=4)

    return {"status": "success"}


@app.get("/alerts")
def get_alerts():

    if not os.path.exists(ALERT_FILE):
        return []

    with open(ALERT_FILE, "r") as f:
        return json.load(f)