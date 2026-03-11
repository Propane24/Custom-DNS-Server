def parse_dns_query(data):

    transaction_id = data[:2]

    index = 12

    labels = []

    while True:

        length = data[index]

        if length == 0:

            break

        index += 1

        labels.append(data[index:index+length].decode())

        index += length

    domain = ".".join(labels)

    return transaction_id, domain


def build_dns_response(transaction_id, query_data, ip):

    header = transaction_id

    header += b'\x81\x80'

    header += b'\x00\x01'

    header += b'\x00\x01'

    header += b'\x00\x00'

    header += b'\x00\x00'

    question = query_data[12:]

    answer = b'\xc0\x0c'

    answer += b'\x00\x01'

    answer += b'\x00\x01'

    answer += b'\x00\x00\x00\x3c'

    answer += b'\x00\x04'

    answer += bytes(map(int, ip.split(".")))

    return header + question + answer
