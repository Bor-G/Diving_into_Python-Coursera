import os
import tempfile

class File:
	def __init__(self, filename):
		self.f = open(filename, 'w+')
		self.filename = filename
		self.current = 0
		self.end = len(self.f.readlines())
		self.f.seek(0)

	def write(self, string):
		self.f.write(string)
	
	def __add__(self, obj):
		storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
		with open(storage_path, 'w') as new_obj:
			new_obj.write(self.f.read())
			new_obj.write(obj.f.read())
		return File(storage_path)

	def __iter__(self):
		return self

	def __next__(self):
		if self.current >= self.end:
			raise StopIteration
		self.current += 1
		return self.f.readline()

	def __str__(self):
		return self.filename



obj = File('5.txt')
obj.write('line\n')

first = File('1.txt')
first.write('line_1\n')
second = File('2.txt')
second.write('line_2\n')
new_obj = first + second
print(File(str(new_obj)))

# obj = File('1.txt')
# print(obj)

# for line in File('1.txt'):
# 	print(line)