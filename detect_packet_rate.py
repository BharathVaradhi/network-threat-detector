import csv
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
        print(f"[ALERT] High traffic from {ip} ({count} packets)")
