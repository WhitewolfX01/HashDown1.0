import crcmod.predefined

# Get the string to hash
input_string = input("Enter a string to hash: ")

# Create a CRC16 hash object
crc16_func = crcmod.predefined.Crc('crc-16')

# Calculate the CRC16 hash of the input string
hash_value = crc16_func.new(input_string.encode()).digest()

# Convert the hash to hexadecimal format
hex_hash = hash_value.hex()

# Print the hash in hexadecimal format
print("CRC16 hash of \"{}\" is:".format(input_string), hex_hash)
