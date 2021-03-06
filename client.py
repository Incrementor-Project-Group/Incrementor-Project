"""Sends random json packets to server over port 5000"""


import socket
import json
from random import randint
from time import time, sleep
from typing import Dict, Any

IP = "192.168.2.104"
PORT = 5000


# -> Dict[str, Any]:
def generate_json_message(data=hash(str(randint(1, 100)))):
    """Generate random json packet with hashed data bits"""
    return {
        "id": randint(1, 100),
        "timestamp": time(),
        "data": data
    }


def send_json_message(
    sock: socket.socket,
    json_message: Dict[str, Any],
):  # -> None:
    """Send json packet to server"""
    message = (json.dumps(json_message) + '\n').encode()
    sock.sendall(message)
    print(f'{len(message)} bytes sent')


def main(data=None):  # -> None
    with socket.socket() as sock:
        sock.connect((IP, PORT))
        json_message = generate_json_message(data)
        send_json_message(sock, json_message)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
