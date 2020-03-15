# -*- coding: cp1251 -*-
# Неблокирующий ввод/вывод, обучающий пример
# Цикл обработки событий в epoll

while True:
    events = epoll.poll(1)
    
    for fileno, event in events:
        if event & select.EPOLLIN:
            # обработка чтения из сокета
            data=conn_map[fileno].recv(1024)
            print(data.decode("utf8"))
        elif event & select.EPOLLOUT:
            # обработка записи в сокет
            conn_map[fileno].send("pong".encode("utf8"))