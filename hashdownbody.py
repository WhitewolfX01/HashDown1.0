def body(hash):
    if(len(hash)==32):
        if(hash.isalnum()):
            print("1. MD6-128\n2. MD5\n3. MD4\n4. MD2\n5. RIPEMD-128\n6. NTLM\n6. Tiger-128,3\n7.Tiger-128,4")
    elif(len(hash)==40):
        if(hash.isalnum()):
            print("1. SHA-1\n2. RIPEMD-160\n3. Tiger-160,3\n4.Tiger-160,4")
    elif(len(hash)==64):
        if(hash.isalnum()):
            print("1. MD6-256\n2. SHA-256\n3. SHA2-512/256\n4. SHA3-256\n5. RIPEMD-256\n6. Shake-128\n7. Snefru\n8. GOST")
    elif(len(hash)==128):
        if(hash.isalnum()):
            print("1. MD6-512\n2. SHA-512\n3. SHA3-512\n4. Whirlpool\n5. Shake-256")
    elif(len(hash)==96):
        if(hash.isalnum()):
            print("1.  SHA-384\n2. SHA3-384")
    elif(len(hash)==56):
        if(hash.isalnum()):
            print("1. SHA-224\n2. SHA2-512/224\n3. SHA3-224")
    elif(len(hash)==80):
        if(hash.isalnum()):
            print("1. RIPEMD-320")
    elif(len(hash)==8):
        if(hash.isalnum()):
            print("1. CRC32\n2. Adler-32\n3. FNV-132\n4. JOAAT")
    elif(len(hash)==4):
        if(hash.isalnum()):
            print("1. CRC16")
    elif(len(hash)==48):
        if(hash.isalnum()):
            print("1. Tiger-192,3\n2. Tiger-192,4")
    elif(len(hash)==16):
        if(hash.isalnum()):
            print("1. FNV-164")
    else:
        print("Sorry!!! Hash can not be recognised...")


st = input("Enter the hash:\n")
print("Possible Hash Types:")
body(st)