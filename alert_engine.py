import csv
import os
from datetime import datetime

ALERT_FILE = "alerts.csv"

if not os.path.exists(ALERT_FILE):
    with open(ALERT_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "timestamp",
            "alert_type",
            "source_ip",
            "severity",
            "description"
        ])


def create_alert(alert_type, source_ip, severity, description):

    with open(ALERT_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            datetime.now().isoformat(),
            alert_type,
            source_ip,
            severity,
            description
        ])

    print(f"[ALERT] {alert_type} | {source_ip} | {severity}")
