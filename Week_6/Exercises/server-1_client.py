def run_server(host, port):
	with socket.socket() as sock:
		sock.bind((host, port))
		sock.listen()
		while True:
			conn, attr = sock.accept()
			with conn:
				while True:
					item = conn.recv(1024)
					if not item:
						break
					item = item.decode("utf8")
					if item[0:3] == "put":
						comm, key, value, timestamp = item.split()
						if key not in data:
							data[key] = []
						data[key].append((int(timestamp), float(value)))
						conn.send("ok\n\n".encode("utf8"))
					elif item[0:3] == "get":
						comm, key = item.split()
						answer = "ok\n"
						if key != "*":
							for metric in data[key]:
								answer += key + ' ' + str(metric[1]) + ' ' + str(metric[0]) + "\n"
						else:
							for key in data:
								for metric in data[key]:
									answer += key + ' ' + str(metric[1]) + ' ' + str(metric[0]) + "\n"
						answer += "\n"
						conn.send(answer.encode("utf8"))
					else:
						conn.send("error\nwrong command\n\n".encode("utf8"))

#run_server("127.0.0.1", 8888)