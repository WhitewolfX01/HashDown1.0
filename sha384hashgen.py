import hashlib

# Get the string to hash
input_string = input("Enter a string to hash: ")

# Convert the string to SHA-384 hash
hash_object = hashlib.sha384(input_string.encode())

# Print the hash in hexadecimal format
print("SHA384 hash of \"{}\" is:".format(input_string), hash_object.hexdigest())