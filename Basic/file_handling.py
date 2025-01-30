# Writing and reading from a file
filename = "jinay_sample.txt"

# Writing to the file
with open(filename, 'w') as f:
    f.write("Hello, Python File Handling!")

# Reading from the file
with open(filename, 'r') as f:
    content = f.read()

print(content)
