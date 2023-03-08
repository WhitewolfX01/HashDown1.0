def hashgen():
    print("--- Hashing Options ---")
    hashlist = ["Adler-32","Base64","CRC-16","CRC-32","MD2","MD4","MD5","RIPEMD-160","SHA-1","SHA-224","SHA-256","SHA-384","SHA-512","SHA3-224","SHA3-256","SHA3-384","SHA3-512","Shake-128","Shake-256"]
    t = 1
    for i in hashlist:
        print("{0}. {1}".format(t,i))
        t+=1
    opt = int(input("\nEnter Your Choice\n>>> "))
    match opt:
        case 1:
            import adler32hashgen
        case 2:
            import base64hashgen
        case 3:
            import crc16hashgen
        case 4:
            import crc32hashgen
        case 5:
            import md2hashgen
        case 6:
            import md4hashgen
        case 7:
            import md5hashgen
        case 8:
            import ripemd160hashgen
        case 9:
            import sha1hashgen
        case 10:
            import sha224hashgen
        case 11:
            import sha256hashgen
        case 12:
            import sha384hashgen
        case 13:
            import sha512hashgen
        case 14:
            import sha3_224hashgen
        case 15:
            import sha3_256hashgen
        case 16:
            import sha3_384hashgen
        case 17:
            import sha3_512hashgen
        case 18:
            import shake128hashgen
        case 19:
            import shake256hashgen
