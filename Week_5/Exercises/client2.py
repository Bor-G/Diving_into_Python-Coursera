import time
import socket
import json

class Client:
    curent_time = time.time()
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    def get(self, key):
        try:
            with socket.create_connection((self.host, self.port),self.timeout) as sock:
                message = 'get {}\n'.format(key)
                sock.sendall(message.encode("utf8"))
                received_data = sock.recv(1024)
                return self._parser(received_data)
        except socket.error:
            raise ClientError("error\nwrong command\n\n")    
            

    def _parser(self, inner_message):
        """Convert inner bite string to dictionary"""
        inner = inner_message.decode("utf8")
        new_dict = dict()
        try:
            if inner == 'ok\n\n':
                return new_dict
            else:
                data_sring = inner.replace("ok\n","").replace("\n\n","").splitlines()
                data_list = []
                for line in data_sring:
                    splitted_line = line.lstrip().split()
                    data_list.append(splitted_line)
                for string in data_list:
                    val = (int(string[2]), float(string[1]),)
                    if string[0] in new_dict:
                        new_dict[string[0]].append(val)
                    else:
                        new_dict[string[0]] = [val]
                return new_dict
        except IndexError:
            raise ClientError("error\nwrong command\n\n")



            

    def put(self, key, value, timestamp=curent_time):
        try:
            with socket.create_connection((self.host, self.port),self.timeout) as sock:
                message = 'put {} {} {}\n'.format(key, value, int(timestamp))
                sock.sendall(message.encode("utf8"))
                received_data = sock.recv(1024)
                return received_data.decode("utf8")
        except socket.error:
            raise ClientError("error\nwrong command\n\n")

        
class ClientError(Exception):
    pass


client = Client("127.0.0.1", 8888, timeout=150)
print(client.put("palm.cpu", 0.5, timestamp=1150864247))