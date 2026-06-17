import csv
from collections import Counter

external_ips = Counter()

with open("packets.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:

        if row["direction"] == "OUTGOING":

            ip = row["destination_ip"]

            if not ip.startswith("192.168."):

                external_ips[ip] += 1

print("\nExternal IP Communication:\n")

for ip, count in external_ips.items():
    print(f"{ip} -> {count} packets")
