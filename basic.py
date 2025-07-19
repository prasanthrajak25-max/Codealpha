from scapy.all import sniff, IP, TCP, UDP, Raw
from datetime import datetime

def packet_callback(packet):
    # Time of capture
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Check if the packet has an IP layer
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        proto = ip_layer.proto

        print(f"\n[+] Time: {timestamp}")
        print(f"[+] Source IP: {src_ip}")
        print(f"[+] Destination IP: {dst_ip}")
        print(f"[+] Protocol: {proto} ({ip_layer.name})")

        # If packet contains TCP or UDP
        if TCP in packet:
            print(f"[+] TCP Src Port: {packet[TCP].sport}")
            print(f"[+] TCP Dst Port: {packet[TCP].dport}")
        elif UDP in packet:
            print(f"[+] UDP Src Port: {packet[UDP].sport}")
            print(f"[+] UDP Dst Port: {packet[UDP].dport}")

        # Print payload (raw data) if available
        if Raw in packet:
            payload = packet[Raw].load
            try:
                print(f"[+] Payload: {payload[:100]}")
            except:
                print("[+] Payload: (unable to decode)")

# Start sniffing
print("Starting packet capture... Press Ctrl+C to stop.\n")
sniff(prn=packet_callback, store=False)
