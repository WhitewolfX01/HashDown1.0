import hashlib

# input string
string = input("Enter the String to hash:")

# create SHA-512 hash object
sha512 = hashlib.sha512()

# update hash object with input string
sha512.update(string.encode())

# get the hex digest of the hash
hash_value = sha512.hexdigest()

# print the hash
print("SHA-512 hash of {} is:".format(string), hash_value)
