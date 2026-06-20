import csv
from alert_engine import create_alert
from collections import Counter

packet_counts = Counter()

with open("packets.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        source_ip = row["source_ip"]
        packet_counts[source_ip] += 1

print("\nPacket Rate Analysis:\n")

for ip, count in packet_counts.items():

    if count > 20:
        create_alert(
    "HIGH_TRAFFIC",
    ip,
    "MEDIUM",
    f"High traffic detected ({count} packets)"
    )
