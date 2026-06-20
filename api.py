import csv
from fastapi import FastAPI
from collections import Counter
app = FastAPI()


@app.get("/alerts")
@app.get("/alerts/{alert_type}")
def get_alerts_by_type(alert_type):

    alerts = []

    with open("alerts.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:

            if row["alert_type"] == alert_type:
                alerts.append(row)

    return alerts
@app.get("/alert-summary")
def alert_summary():

    counts = Counter()

    with open("alerts.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            counts[row["alert_type"]] += 1

    return dict(counts)
def get_alerts():

    alerts = []

    with open("alerts.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            alerts.append(row)

    return alerts
