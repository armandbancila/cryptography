def caesar(text, shift):
    cipherText = list(map(lambda x: chr((ord(x) - 97 + shift) % 26 + 97), text.lower()))
    return ''.join(cipherText)

def vigenere(text, password):
    cipherText = list(map(lambda i: caesar(text[i], ord(password[i % len(password)].lower()) - 97), range(len(text))))
    return ''.join(cipherText)

print(vigenere('textt', 'oink'))

