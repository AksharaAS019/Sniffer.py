from scapy.all import *

def packet_callback(packet):
    print(packet.summary())

print("Sniffing packets... Press Ctrl+C to stop")
sniff(prn=packet_callback, count=10)