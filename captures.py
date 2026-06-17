import csv
import os
from scapy.all import sniff, IP, TCP, UDP
from datetime import datetime
MY_IP = "192.168.31.112"

def packet_callback(packet):

    if IP in packet:
          
          if packet[IP].src == MY_IP:
            direction = "OUTGOING"

          elif packet[IP].dst == MY_IP:
           direction = "INCOMING"

          else:
           direction = "OTHER"
          packet_data = {
            "source_ip": packet[IP].src,
            "destination_ip": packet[IP].dst,
            "protocol": None,
            "source_port": None,
            "destination_port": None,
            "packet_size": len(packet),
            "timestamp": datetime.now().isoformat(),
            "direction":direction
        }
        
         
        

          if TCP in packet:
            packet_data["protocol"] = "TCP"
            packet_data["source_port"] = packet[TCP].sport
            packet_data["destination_port"] = packet[TCP].dport

          elif UDP in packet:
            packet_data["protocol"] = "UDP"
            packet_data["source_port"] = packet[UDP].sport
            packet_data["destination_port"] = packet[UDP].dport

          with open(csv_file, "a", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                packet_data["source_ip"],
                packet_data["destination_ip"],
                packet_data["protocol"],
                packet_data["source_port"],
                packet_data["destination_port"],
                packet_data["packet_size"],
                packet_data["timestamp"],
                packet_data["direction"]
            ])

          print("\n{")

          for key, value in packet_data.items():
            print(f"{key}: {value}")

          print("}")

csv_file = "packets.csv"

if not os.path.exists(csv_file):
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            
            "source_ip",
            "destination_ip",
            "protocol",
            "source_port",
            "destination_port",
            "packet_size",
            "timestamp",
            "direction"
        ])
sniff(prn=packet_callback, count=5)