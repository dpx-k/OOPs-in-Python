# The print function is used to print data into the console 
print ("Deepak", 19)

# The default separator is the whitespace " ", you can change it 
print("Prateek", 12, sep = ", ")
print("Anushka", 20, sep = "\n")

# by default python adds the \n tag at the end of each print statement, you change it too 
print()

print("Deepak", end = " ")
print("Prateek")


# The print function can take multiple arguments, and it will print them all
print("Deepak", 19, "Prateek", 12, "Anushka", 20)

# The print function can also take a file argument, which allows you to write to a file instead of the console
with open("output.txt", "w") as f:
    print("Hello, World!", file=f)

#The print function can also take a flush argument, which allows you to flush the output buffer
print("Hello, World!", flush=True)

# The print function can also take a format argument, which allows you to format the output
print("Hello, {}!".format("World"))

# The print function can also take a f-string argument, which allows you to format the output using f-strings
name = "World"
print(f"Hello, {name}!")  