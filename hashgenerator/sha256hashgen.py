import hashlib

string = input("Enter a string to hash: ")

# Encode the string as bytes before hashing
encoded_string = string.encode('utf-8')

# Create a SHA-256 hash object and hash the encoded string
sha256_hash = hashlib.sha256(encoded_string)

# Get the hexadecimal representation of the hash
hex_hash = sha256_hash.hexdigest()

print(f"SHA-256 hash of \"{string}\": {hex_hash}")
