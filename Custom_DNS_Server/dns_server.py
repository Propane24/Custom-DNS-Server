import socket
import threading
import json
from dns_parser import parse_dns_query, build_dns_response

PORT = 8053

with open("records.json") as f:
    LOCAL_RECORDS = json.load(f)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", PORT))

print("DNS Server running on port", PORT)

def handle_query(data, addr):

    try:
        transaction_id, domain = parse_dns_query(data)

        print("Query from", addr, "for", domain)

        if domain in LOCAL_RECORDS:

            ip = LOCAL_RECORDS[domain]

            response = build_dns_response(transaction_id, data, ip)

            sock.sendto(response, addr)

        else:

            upstream = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            upstream.settimeout(3)

            upstream.sendto(data, ("8.8.8.8", 53))

            response, _ = upstream.recvfrom(512)

            sock.sendto(response, addr)

    except Exception as e:

        print("Error handling request:", e)


while True:

    data, addr = sock.recvfrom(512)

    thread = threading.Thread(target=handle_query, args=(data, addr))

    thread.start()
