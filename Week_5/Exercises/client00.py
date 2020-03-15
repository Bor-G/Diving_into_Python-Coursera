import socket
import time

class Client:
    def __init__(self, host, port, timeout=None):
        self.sock = socket.create_connection((host, port), timeout)
    
    def put(self, key, value, timestamp=None):
        if timestamp is None:
            timestamp = str(int(time.time()))
        string = "put " + key + " " + str(value) + " " + str(timestamp) + "\n"
        self.sock.sendall(string.encode("utf8"))
        answer = self.sock.recv(1024).decode("utf8")
        if answer != "ok\n\n":
            raise ClientError 
    
    def get(self, key):
        string = "get " + key + "\n"
        self.sock.sendall(string.encode("utf8"))
        answer = self.sock.recv(1024).decode("utf8")
        if answer[0:2] != "ok":
            raise ClientError 
        data = {}
        if answer != "ok\n\n":
            items = answer.split("\n")
            for item in items[1:-2]:
                key_ex, value, timestamp = item.split()
                if key_ex not in data:
                    data[key_ex] = []
                data[key_ex].append((int(timestamp), float(value)))
        return data


class ClientError(Exception):
    pass


client = Client("127.0.0.1", 8888, timeout=15)
client.put("palm.cpu", 0.5, timestamp=1150864247)
client.put("palm.cpu", 2.0, timestamp=1150864248)
client.put("palm.cpu", 0.5, timestamp=1150864248)
client.put("eardrum.cpu", 3, timestamp=1150864250)
client.put("eardrum.cpu", 4, timestamp=1150864251)
client.put("eardrum.memory", 4200000)
print(client.get("*"))