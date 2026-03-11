import struct


def parse_dns_query(data):

    transaction_id = data[:2]

    index = 12
    domain_parts = []

    while True:
        length = data[index]
        if length == 0:
            break

        index += 1
        domain_parts.append(data[index:index+length].decode())
        index += length

    domain = ".".join(domain_parts)

    return transaction_id, domain


def build_dns_response(transaction_id, query_data, ip):

    # DNS header
    header = transaction_id
    header += b'\x81\x80'  # flags
    header += b'\x00\x01'  # questions
    header += b'\x00\x01'  # answers
    header += b'\x00\x00'  # authority
    header += b'\x00\x00'  # additional

    # Extract question section properly
    index = 12

    while query_data[index] != 0:
        index += 1

    index += 5  # null byte + qtype + qclass

    question = query_data[12:index]

    # Answer section
    answer = b'\xc0\x0c'  # pointer to domain name
    answer += b'\x00\x01'  # type A
    answer += b'\x00\x01'  # class IN
    answer += b'\x00\x00\x00\x3c'  # TTL
    answer += b'\x00\x04'  # data length
    answer += bytes(map(int, ip.split(".")))

    return header + question + answer
