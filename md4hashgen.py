import hashlib

string = input("Enter a string to hash: ")

# Encode the string as bytes before hashing
encoded_string = string.encode('utf-8')

# Create an MD4 hash object and hash the encoded string
md4_hash = hashlib.new('md4', encoded_string)

# Get the hexadecimal representation of the hash
hex_hash = md4_hash.hexdigest()

print(f"MD4 hash of \"{string}\": {hex_hash}")
