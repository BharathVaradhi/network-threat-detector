import csv
from alert_engine import create_alert
from collections import defaultdict

ip_ports = defaultdict(set)

with open("packets.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:

        source_ip = row["source_ip"]

        if source_ip.startswith("192.168."):

            ip_ports[source_ip].add(
                row["destination_port"]
            )

THRESHOLD = 5

print("\nPort Scan Alerts:\n")

for ip, ports in ip_ports.items():

    print(ip, len(ports), ports)

    if len(ports) > THRESHOLD:
         create_alert(
    "PORT_SCAN",
    ip,
    "MEDIUM",
    f"Accessed {ports} unique destination ports"
       )
