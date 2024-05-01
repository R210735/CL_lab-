# Writing to a file
with open('example.txt', 'w') as f:
    f.write('Hello, world!\n')
    f.write('This is a sample text file.\n')

# Reading from a file
with open('example.txt', 'r') as f:
    for line in f:
        print(line.strip())  # Strip newline character

