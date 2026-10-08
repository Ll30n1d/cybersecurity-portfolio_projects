from scapy.all import IP, TCP, send

def main():
    target_ip = "127.0.0.1"
    target_port = 12345
    message = "Dear Steel Cat! This is no attack, it's my humster Pinkie you should track"

    packet = IP(dst=target_ip) / TCP(dport=target_port, flags="PA") / message

    send(packet)

if __name__ == "__main__":
    main()