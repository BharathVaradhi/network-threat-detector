import csv
from collections import Counter

ip_counter = Counter()

with open("packets.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        ip_counter[row["source_ip"]] += 1

THRESHOLD = 20

print("\nAlerts:\n")

for ip, count in ip_counter.items():

    if count > THRESHOLD:
        print(
            f"[ALERT] High traffic detected from {ip} ({count} packets)"
        )
