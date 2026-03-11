# Custom-DNS-Server

A lightweight DNS server implementation using UDP sockets built for learning network programming and protocol design.

The server can resolve local DNS records and forward unknown requests to an upstream DNS server while supporting multiple concurrent clients.

Features

UDP socket DNS server

DNS packet parsing

Local domain resolution

Recursive DNS query forwarding

Multi-client support using threads

Performance benchmarking

Configurable local DNS records

System Architecture
                +-------------+
                |   Client    |
                |   (dig)     |
                +------+------+
                       |
                  DNS Query
                       |
                       v
            +----------------------+
            |   Custom DNS Server  |
            |  UDP Port 8053       |
            +----------+-----------+
                       |
         --------------------------------
         |                              |
 Local DNS Resolution          Recursive Forwarding
  (records.json)               to Google DNS (8.8.8.8)

Project Structure
custom_dns_server_project
│
├── dns_server.py
├── dns_parser.py
├── performance_test.py
├── records.json
└── README.md

File Description
File	Description
dns_server.py	Main DNS server implementation
dns_parser.py	DNS packet parsing and response construction
records.json	Local DNS database
performance_test.py	Script for benchmarking DNS queries
Requirements

Python 3.x

dig (DNS testing utility)

Installing Dependencies
MacOS
brew install bind

Ubuntu / Linux
sudo apt install dnsutils

Verify Installation
dig google.com

Running the DNS Server

Navigate to the project directory:

cd custom_dns_server_project


Start the server:

python3 dns_server.py


Expected output:

DNS Server running on port 8053


The server is now listening for DNS queries on UDP port 8053.

Testing the DNS Server

Open another terminal.

Local DNS Resolution
dig example.com @127.0.0.1 -p 8053


Expected result:

example.com -> 192.168.1.100

Recursive DNS Forwarding
dig google.com @127.0.0.1 -p 8053


If the domain is not in records.json, the query will be forwarded to Google Public DNS (8.8.8.8).

Handling Multiple Clients

The server supports concurrent clients using multithreading.

Each incoming request is handled by a separate thread, allowing the server to process multiple DNS queries simultaneously.

Example test:

for i in {1..20}; do dig google.com @127.0.0.1 -p 8053 & done


Server log example:

Query from ('127.0.0.1', 50123)
Query from ('127.0.0.1', 50124)
Query from ('127.0.0.1', 50125)

Performance Evaluation

Run the benchmark script:

python3 performance_test.py


Example output:

Total queries: 100
Total time: 1.85 seconds
Queries per second: 54

Metrics Measured

Response time

Throughput (queries per second)

Concurrent request handling

Local DNS Records

Local DNS mappings are stored in:

records.json


Example configuration:

{
  "example.com": "192.168.1.100",
  "test.com": "192.168.1.200",
  "myserver.local": "127.0.0.1"
}


You can add more domains by editing this file.

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


Run performance test

python3 performance_test.py

Learning Objectives

This project demonstrates key networking concepts including:

socket programming

DNS protocol basics

UDP communication

concurrent server design

performance evaluation

Future Improvements

Possible enhancements:

DNS caching

DNSSEC validation

TLS encrypted DNS (DNS-over-TLS)

logging and monitoring

rate limiting
