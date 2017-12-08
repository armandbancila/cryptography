def caesar(text, shift):
    cipherText = list(map(lambda x: chr((ord(x) - 97 + shift) % 26 + 97), text.lower()))
    return ''.join(cipherText)

print(caesar("abcxyz", 1))
print(caesar(caesar("abcxyz", 13), 13))

