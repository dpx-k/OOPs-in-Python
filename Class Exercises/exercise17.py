# File Handling; writing and reading a file

# Open a file in write mode ('w') and write some text to it
with open("example_file.txt", "w") as file:
    file.write("Hello, this is a simple file.\n")
    file.write("This demonstrates file open and closing in Python.\n")
    print("Data has been written to the file.")

# Open the file again in read mode ('r') to read its contents
with open("example_file.txt", "r") as file:
    content = file.read() # Read the entire content of the file
    print("Contents of the file:")
    print(content)
