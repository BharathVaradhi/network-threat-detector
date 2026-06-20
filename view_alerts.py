import csv
from collections import Counter

alert_counts = Counter()

print("\nStored Alerts:\n")

with open("alerts.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:

        print(
            f"{row['alert_type']} | "
            f"{row['source_ip']} | "
            f"{row['severity']}"
        )

        alert_counts[row["alert_type"]] += 1

print("\nAlert Summary:\n")

for alert_type, count in alert_counts.items():

    print(f"{alert_type}: {count}")
