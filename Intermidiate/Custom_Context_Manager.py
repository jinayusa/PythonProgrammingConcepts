# Creating a custom context manager using __enter__ and __exit__
class FileOpener:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

# Using the custom context manager
with FileOpener('test.txt', 'w') as f:
    f.write("This is a test.")

# Reading the file
with FileOpener('test.txt', 'r') as f:
    content = f.read()

print(content)
