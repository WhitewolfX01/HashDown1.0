import hashlib

# Get the string to hash
input_string = input("Enter a string to hash: ")

# Convert the string to SHAKE128 hash
hash_object = hashlib.shake_128(input_string.encode())

# Print the hash in hexadecimal format
print("Shake-128 hash of \"{}\" is:".format(input_string), hash_object.hexdigest(32))