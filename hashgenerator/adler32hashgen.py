import zlib

# Get the string to hash
input_string = input("Enter a string to hash: ")

# Calculate the Adler-32 hash of the input string
hash_value = zlib.adler32(input_string.encode())

# Print the hash value
print("Adler-32 hash of \"{0}\" is :".format(input_string), hex(hash_value))
print("Note: Ignore the 'x' in the hash value. Only consider the rest 8 characters.")
