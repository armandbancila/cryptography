from hashlib import sha1, sha256, sha384, sha512
from binascii import hexlify

def xor(x, y):
    return bytes(x ^ y for x, y in zip(x, y))

def hmac(key, message, outputLength, prf):
    # pseudorandom function
    prf = prf or sha256
    # blocksize of the input to the prf
    # 64 bytes for MD5, SHA-1, SHA-224, SHA-256, and 128 bytes for SHA-384 and SHA-512, per RFC2104 and RFC4868    
    if prf == sha384 or prf == sha512:
        blockSize = 128
    else:
        blockSize = 64
    # if key too big, run it through prf
    if len(key) > blockSize:
        key = prf(key).digest()
    # append blocksize - len(key) zeroes to the key
    key = key + bytes.fromhex('00' * (blockSize - len(key)))
    # generate padding
    innerPadding = bytes.fromhex('36') * blockSize
    outerPadding = bytes.fromhex('5c') * blockSize
    # computer MAC over message using HMAC function
    dk = prf(xor(key, outerPadding) + prf(xor(key, innerPadding) + message).digest()).digest()
    return dk

# should be '4f4ca3d5d68ba7cc0a1208c9c61e9c5da0403c0a'
# from NIST's test vectors
key = '000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f202122232425262728292a2b2c2d2e2f303132333435363738393a3b3c3d3e3f'
key = bytes.fromhex(key)
message = b'Sample #1'
x = hmac(key, message, 32, sha1)
print(hexlify(x))

