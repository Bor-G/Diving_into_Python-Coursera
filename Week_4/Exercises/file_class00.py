# -*- coding: cp1251 -*-
"""�������
� ���� ������� ����� ���� ��������� ����������� ��������� ������������ 
���������� ������� � ���� �������. ��� ������������� �� ��������� ����, � 
����� ����� ��������� ������������� �����, ���� ��� � �� ����������� ��� 
������������. ������ write � read ������ �������� � ������ � �������. ���� 
������� ������ ��� ������ �� �����������, ��� ���������� �������� ��� � ������ 
������ �������, �� � ������ � ����� write ��� read.

����� __str__ ���� �� ������ � ��� ��������, ��������� ������ ����� ���������. 
��� �������� ������ �� ��� ������� ������ ������ ����� ������ �����. � ������� 
��� ���������� ������ �� �������, � � �������� ������� ����� ������ ��� ������ 
�������� ���������� ������ ��������������. � ������� �� ������� ��� � ������� 
������ uuid, ������� ��������� ��������� �������������� UUID. ���� �� ��������� 
� ��� �� ����������, ��� � ������������, ��� �������� �������� ������� � ������� 
(����� ������������ gettempdir ��� � �������).

��� �������� ������� �������� �������� ���������� ������ ����������� ������. 
����� ������� ��������� ���� �� ������ ������� �������� �����, ��������, � 
������� ������ readlines. ������, � ����� ������ �� ������ ����� ���� ����, 
������� ����� ���� ����� ������� � ������� ���� ��� ����� ���� � �� �����. 
� ����� ������� �� ��������� ������� ������� � ����� � ������� ������ tell � 
���������� readline ��� ��������� ������������ ��������� ������. �� ��������� 
������ ����� ����� ����������� StopIteration, ��� ������ ��������� ���� 
��������. ����� ���� ����� ������������ ��, ��� �������� ������ � Python ��� 
�� ���� �������� ����������.
"""

import os
import tempfile
import uuid


class File:
    def __init__(self, path):
        self.path = path
        self.current_position = 0

        if not os.path.exists(self.path):
            open(self.path, 'w').close()

    def write(self, content):
        with open(self.path, 'w') as f:
            return f.write(content)

    def read(self):
        with open(self.path, 'r') as f:
            return f.read()

    def __add__(self, obj):
        new_path = os.path.join(
            tempfile.gettempdir(),
            str(uuid.uuid4().hex)
        )
        new_file = type(self)(new_path)
        new_file.write(self.read() + obj.read())

        return new_file

    def __str__(self):
        return self.path

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path, 'r') as f:
            f.seek(self.current_position)

            line = f.readline()
            if not line:
                self.current_position = 0
                raise StopIteration('EOF')

            self.current_position = f.tell()
            return line


obj = File('5.txt')
obj.write('line\n')

first = File('1.txt')
first.write('line_1\nline2\n')
second = File('2.txt')
second.write('line_3\nline4\n')
new_obj = first + second
print(File(str(new_obj)))

# obj = File('1.txt')
# print(obj)

# for line in File('1.txt'):
# 	print(line)