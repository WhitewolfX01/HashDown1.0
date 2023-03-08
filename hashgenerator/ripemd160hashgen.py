from Crypto.Hash import RIPEMD160

# Get the string to hash
input_string = input("Enter a string to hash: ")

# Convert the string to RIPEMD-160 hash
hash_object = RIPEMD160.new(input_string.encode())

# Print the hash in hexadecimal format
print("RIPEMD-160 hash of \"{}\" is:".format(input_string), hash_object.hexdigest())
