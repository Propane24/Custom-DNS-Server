Custom DNS Server (UDP Socket Programming)




A lightweight DNS server implemented using UDP sockets.
This project demonstrates low-level networking concepts, DNS packet parsing, and concurrent client handling.

Features

UDP socket DNS server
DNS packet parsing
Local domain resolution
Recursive DNS query forwarding
Multi-client support using threads
Performance benchmarking
Configurable local DNS records

System Architecture
```
+-----------+
|  Client   |
|  (dig)    |
+-----+-----+
      |
      v
+-----------------------+
|  Custom DNS Server    |
|    UDP Port 8053      |
+----------+------------+
           |
     -----------------
     |               |
     v               v
Local DNS       Forward Query
(records.json)  to Google DNS
                (8.8.8.8)
```
Project Structure
```

custom_dns_server_project
│
├── dns_server.py
├── dns_parser.py
├── performance_test.py
├── records.json
└── README.md
```


Requirements

1.Python 3.x
2.dig (DNS testing utility)


Running the DNS Server

Navigate to the project directory:

      cd custom_dns_server_project


Start the server:

      python3 dns_server.py


Expected output:

      DNS Server running on port 8053


The DNS server will now listen for queries on UDP port 8053.

Testing the DNS Server:

Open another terminal window.

Test Local DNS Resolution

      dig example.com @127.0.0.1 -p 8053


Expected output:

      example.com -> 192.168.1.100


This domain is resolved from records.json.

Test Recursive DNS Forwarding

      dig google.com @127.0.0.1 -p 8053


If the domain is not found locally, the server forwards the request to Google DNS (8.8.8.8).

Multiple Client Support

The server supports multiple concurrent clients using multithreading.

To simulate multiple users:

for i in {1..20}; do dig google.com @127.0.0.1 -p 8053 & done


Example server output:

      Query from ('127.0.0.1', 50123)
      Query from ('127.0.0.1', 50124)
      Query from ('127.0.0.1', 50125)


Each query is processed in a separate thread.


Performance Evaluation

Run the performance benchmarking script:

      python3 performance_test.py


Example output:

      Total queries: 100
      Total time: 1.8 seconds
      Queries per second: 55

Metrics Measured

Response Time
Throughput (Queries per second)
Concurrent request handling
Local DNS Records
Local DNS mappings are stored in:
records.json


Example configuration:
```
{
  "example.com": "192.168.1.100",
  "test.com": "192.168.1.200",
  "myserver.local": "127.0.0.1"
}
```

Error Handling

The server includes basic handling for:

invalid DNS packets
upstream DNS timeouts
malformed requests
socket errors

Demonstration Steps

Start the DNS server

      python3 dns_server.py


Query a local domain

      dig example.com @localhost -p 8053


Query an external domain

      dig google.com @localhost -p 8053


Run performance benchmark

      python3 performance_test.py


