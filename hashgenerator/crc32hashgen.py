import binascii

# Get the string to hash
input_string = input("Enter a string to hash: ")

# Convert the string to CRC32 hash
hash_value = binascii.crc32(input_string.encode())

# Convert the hash to hexadecimal format
hex_hash = hex(hash_value)[2:]

# Print the hash in hexadecimal format
print("CRC32 hash of \"{}\" is:".format(input_string), hex_hash)
