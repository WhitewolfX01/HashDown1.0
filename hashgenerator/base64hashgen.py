import base64

# Get the string to hash
input_string = input("Enter a string to hash: ")

# Calculate the base64 hash of the input string
hash_value = base64.b64encode(input_string.encode())

# Print the hash value
print("Base64 hash of \"{}\" is:".format(input_string), hash_value.decode())
