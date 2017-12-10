def lsz40(plaintext, key):
    # international telepgrah alphabet code
    ita2 = [24, 19, 14, 18, 16, 22, 11, 5, 12, 26, 30, 9, 7, 6, 3, 13, 29, 10, 20, 1, 28, 15, 25, 23, 21, 17, 2, 8, 31, 4, 27, 0]
    ltrs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ34-.+/9 85"

    boolify = lambda x: list(map(lambda c: bool(int(c)), x))
    k = list(map(boolify, key[:5]))
    s = list(map(boolify, key[5:10]))
    m = list(map(boolify, key[10:12]))

    intify = lambda x: list(map(int, x))
    kPos = intify(key[12].split(' '))
    sPos = intify(key[13].split(' '))
    mPos = intify(key[14].split(' '))
    
    cipherText = ''
    plaintext = plaintext.upper()
    for letter in plaintext:
        # each of the k wheels operates on a single bit of the plaintext
        # for the sake of simplicity, treat the k and s wheels as 2 binary numbers
        kWheelsCode = sWheelsCode = 0
        for i in range(5):
            kWheelsCode = (kWheelsCode << 1) + k[i][kPos[i]]
            sWheelsCode = (sWheelsCode << 1) + s[i][sPos[i]]

        # first XOR the letter with the k wheels, then with the s wheels
        letterCode = ita2[ltrs.index(letter)]
        encryptedLetter = letterCode ^ kWheelsCode ^ sWheelsCode

        # turn the wheels
        if (m[1][mPos[1]]):
            for i in range(5):
                sPos[i] = (sPos[i] + 1) % len(s[i])

        if (m[0][mPos[0]]):
            mPos[1] = (mPos[1] + 1) % len(m[1])

        mPos[0] = (mPos[0] + 1) % len(m[0])

        for i in range(5):
            kPos[i] = (kPos[i] + 1) % len(k[i])

        cipherText += ltrs[ita2.index(encryptedLetter)]

    return cipherText

key1 = ['01100111000011100111000010011011000110110', '0001100110001011110111000011011', '01111011000111000110001100100', '10100111010011000110010101', '10100001110100011110010', '0001110011100111100011000110011100011001011', '11010011100111001100011110001110011001110001000', '111001100011000111000100011110001001110011100110010', '10111001100011001001110011000100011110011100110011100', '01100010011100110011100110001111001001110011110001000111001', '1010101111010101110111011101101101101101110101011101110101101', '1110111011101011011101110110101101010']

kPos = ['1 1 1 3 1']
sPos = ['20 38 38 33 46']
mPos = ['21 14']

key1 = key1 + kPos + sPos + mPos

text1 = "ABCDEFGHIJKLMNO"

print(lsz40(text1, key1))
print(lsz40(lsz40(text1, key1), key1))

