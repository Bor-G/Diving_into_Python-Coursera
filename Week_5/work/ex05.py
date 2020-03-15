# -*- coding: cp1251 -*-
# ������������� ����/�����, ��������� ������

import socket
import select

sock = socket.socket()
sock.bind(("", 10001))
sock.listen()

# ��� ���������� ������� ��� conn1 � conn2
# ������������ ��� �������?
conn1, addr = sock.accept()
conn2, addr = sock.accept()

conn1.setblocking(0)
conn2.setblocking(0)
    
epoll = select.epoll()
epoll.register(conn1.fileno(), select.EPOLLIN | select.EPOLLOUT)
epoll.register(conn2.fileno(), select.EPOLLIN | select.EPOLLOUT)

conn_map = {
    conn1.fileno(): conn1,
    conn2.fileno(): conn2,
}