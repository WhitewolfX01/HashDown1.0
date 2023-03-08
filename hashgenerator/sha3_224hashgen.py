import hashlib

# Get the string to hash
input_string = input("Enter a string to hash: ")

# Convert the string to SHA3-224 hash
hash_object = hashlib.sha3_224(input_string.encode())

# Print the hash in hexadecimal format
print("SHA3-224 hash of \"{}\" is:".format(input_string), hash_object.hexdigest())
