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
            import hashgenerator.adler32hashgen
        case 2:
            import hashgenerator.base64hashgen
        case 3:
            import hashgenerator.crc16hashgen
        case 4:
            import hashgenerator.crc32hashgen
        case 5:
            import hashgenerator.md2hashgen
        case 6:
            import hashgenerator.md4hashgen
        case 7:
            import hashgenerator.md5hashgen
        case 8:
            import hashgenerator.ripemd160hashgen
        case 9:
            import hashgenerator.sha1hashgen
        case 10:
            import hashgenerator.sha224hashgen
        case 11:
            import hashgenerator.sha256hashgen
        case 12:
            import hashgenerator.sha384hashgen
        case 13:
            import hashgenerator.sha512hashgen
        case 14:
            import hashgenerator.sha3_224hashgen
        case 15:
            import hashgenerator.sha3_256hashgen
        case 16:
            import hashgenerator.sha3_384hashgen
        case 17:
            import hashgenerator.sha3_512hashgen
        case 18:
            import hashgenerator.shake128hashgen
        case 19:
            import hashgenerator.shake256hashgen
