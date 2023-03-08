import hashlib

# Get the string to hash
input_string = input("Enter a string to hash: ")

# Convert the string to SHA3-512 hash
hash_object = hashlib.sha3_512(input_string.encode())

# Print the hash in hexadecimal format
print("SHA3-512 hash of \"{}\" is:".format(input_string), hash_object.hexdigest())