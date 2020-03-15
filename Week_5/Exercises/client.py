import socket
import time

class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        try:
            self.connection = socket.create_connection((host, port), timeout)
        except socket.error as err:
            raise ClientError("error create connection", err)

    def _read(self):
        data = b""
        while not data.endswith(b"\n\n"):
            try:
                data += self.connection.recv(1024)
            except socket.error as err:
                raise ClientError("error recv data", err)
        decoded_data = data.decode()
        status, content = decoded_data.split("\n", 1)
        content = content.strip()
        if status == "error":
            raise ClientError(content)
        return content

    def put(self, key, value, timestamp=None):
        timestamp = timestamp or int(time.time())
        try:
            self.connection.sendall(
                f"put {key} {value} {timestamp}\n".encode()
            )
        except socket.error as err:
            raise ClientError("error send data", err)
        self._read()

    def get(self, key):
        try:
            self.connection.sendall(
                f"get {key}\n".encode()
            )
        except socket.error as err:
            raise ClientError("error send data", err)
        content = self._read()
        data = {}
        if content == "":
            return data
        for row in content.split("\n"):
            key, value, timestamp = row.split()
            if key not in data:
                data[key] = []
            data[key].append((int(timestamp), float(value)))
        return data

    def close(self):
        try:
            self.connection.close()
        except socket.error as err:
            raise ClientError("error close connection", err)

class ClientError(Exception):
    pass