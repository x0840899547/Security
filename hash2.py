import hashlib
hashObject = hashlib.sha1()
hashObject.update("hello")
print(hashObject.hexdigest())