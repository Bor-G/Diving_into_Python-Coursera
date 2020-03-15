import socket
import json

metrics = {'palm.cpu':[(1150864247, 0.5),(1150864248, 0.5)],'eardrum.cpu':[(1150864250, 3.0),(1150864251, 4.0)],'eardrum.memory':[(1503320872, 4200000.0)]}

json_object = json.dumps(metrics, sort_keys=True)
#print(json_object)
print("I'm working")

with socket.socket() as sock:
    sock.bind(("", 10001))
    sock.listen(1)
    while True:
        conn, addr = sock.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                message = "\nok recived: {}\n\n".format(data.decode("utf8"))
                print(message)
                send_data = conn.sendall(message.encode("utf8"))