from Crypto.Hash import MD2

text = input("Enter a string to hash : ")
hashObject = MD2.new()
hashObject.update(text.encode('utf-8'))
digest = hashObject.hexdigest()
print("MD2 hash of \"{}\" is:".format(text), digest)