class FileReader:
    def __init__(self, name):
        self.name = name

    def read(self):
        try:
            with open(self.name, "r") as f:
                return f.read()
        except IOError:
            return ""