import hashlib

string = input("Enter a string to hash: ")

# Encode the string as bytes before hashing
encoded_string = string.encode('utf-8')

# Create an MD5 hash object and hash the encoded string
md5_hash = hashlib.md5(encoded_string)

# Get the hexadecimal representation of the hash
hex_hash = md5_hash.hexdigest()

print(f"MD5 hash of \"{string}\": {hex_hash}")
