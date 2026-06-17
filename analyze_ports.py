import csv
from collections import Counter

port_counter = Counter()

with open("packets.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        port_counter[row["destination_port"]] += 1

print("\nTop Destination Ports:\n")

for port, count in port_counter.most_common():
    print(f"Port {port}: {count} packets")
