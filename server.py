"""
Server-Side that receives json packets from client over the network using port 5000.
"""
import random
import string
import json
from socketserver import StreamRequestHandler, TCPServer


def save_json(data: bytes):
    """Saves json packets to file and name it with id"""
    filename = ''.join('current_status') + '.json'
    with open(filename, 'wb') as f:
        f.write(data)
    print('saved to', filename)


def parse_json_message(raw_data: bytes):  # -> Dict[str, Any]
    """Parse raw data from socket into json object"""
    return json.loads(raw_data.decode())


class DumpHandler(StreamRequestHandler):
    def handle(self):
        """receive json packets from client"""
        print('connection from {}:{}'.format(*self.client_address))
        try:
            while True:
                data = self.rfile.readline()
                if not data:
                    break
                print('received', data.decode().rstrip())
                save_json(data)  # uncomment to save json packets as files
                parse_json_message(data)
        finally:
            print('disconnected from {}:{}'.format(*self.client_address))


def main():
    server_address = ('0.0.0.0', 5000)
    print('starting up on {}:{}'.format(*server_address))
    with TCPServer(server_address, DumpHandler) as server:
        print('waiting for a connection')
        server.serve_forever()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
