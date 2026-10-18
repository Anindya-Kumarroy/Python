# Open the file in read mode
f = open("demo.txt", "r")

# Read the whole content of the file and store it in data
data = f.read()

# Print the content that was read
print(data)

# Print the type of data (it will be str)
print(type(data))

# Close the file since we are done with it
f.close()