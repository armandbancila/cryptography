def lsz42(plaintext, key):
    # international telepgrah alphabet code
    ltrs = ' E\nA SIU\rDRJNFCKTZLWHYPQOBG#MXV@'
    # fig = "3\n- '87\r~4^,!:(5+)2$6019?&#./;@"
    # ita2 = {'': 0}
    # ita2.update(dict(zip(ltr, range(1, 32))))
    # ita2.update(dict(zip(fig, range(1, 32))))

    # initialize all the cams on the wheels to 0
    # all wheels start at position 0
    # k / chi wheels
    boolify = lambda x: list(map(lambda c: bool(int(c)), x.split(' ')))
    k = list(map(boolify, key[:5]))
    s = list(map(boolify, key[5:10]))
    m = list(map(boolify, key[10:12]))
    kPos = boolify(key[12])
    sPos = boolify(key[13])
    mPos = boolify(key[14])
    
    cipherText = ''
    plaintext = plaintext.upper()
    for letter in plaintext:
        # each of the k wheels operates on a single bit of the plaintext
        # for the sake of simplicity, treat the k and s wheels as 2 binary numbers
        kWheelsCode = 0
        sWheelsCode = 0
        for i in range(5):
            kWheelsCode = (kWheelsCode << 1) + k[i][kPos[i]]
            sWheelsCode = (sWheelsCode << 1) + s[i][sPos[i]]
        
        # first XOR the letter with the k wheels, then with the s wheels
        letterCode = ltrs.index(letter)
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

        cipherText += (ltrs[encryptedLetter])
    return cipherText

k = ["0 0 0 1 1 1 1 0 0 0 0 1 1 0 0 0 0 1 0 1 1 0 0 1 0 0 1 1 0 1 0 1 1 0 1 0 1 1 1 1 0",
'1 1 0 0 1 1 1 0 1 1 0 0 0 1 0 1 0 1 1 0 0 0 1 0 0 0 0 1 1 1 0',
'0 0 1 1 1 0 1 1 0 0 1 0 0 0 0 1 1 1 0 0 1 1 0 1 1 0 0 1 1',
'0 0 1 1 0 0 1 0 1 1 0 0 1 0 0 1 1 0 0 1 0 0 1 1 1 1',
'0 1 0 0 0 1 0 1 1 0 0 1 0 0 0 1 1 1 0 1 1 1 0']

s = ['0 0 1 0 1 0 1 0 1 0 1 0 0 1 0 0 1 0 1 1 0 1 1 0 1 0 1 0 0 1 1 0 1 1 1 0 0 1 1 1 0 0 0',
'0 0 1 0 1 1 0 1 0 1 0 1 0 1 0 1 0 1 1 0 0 1 1 0 1 0 0 1 0 1 1 1 1 0 0 0 0 0 1 1 1 0 0 1 0 1 1',
'1 0 1 0 1 0 1 0 1 0 1 0 1 0 0 1 0 0 1 1 0 1 0 1 0 1 1 1 1 0 0 0 0 1 1 1 0 0 0 1 1 1 0 1 1 0 0 1 0 0 1',
'1 0 1 0 0 1 1 0 1 0 1 0 1 0 1 0 1 0 1 1 0 1 0 0 0 0 1 1 0 0 1 1 0 0 1 1 0 1 1 1 1 1 0 1 0 0 1 0 0 0 0 1 0',
'0 1 0 1 0 1 0 1 0 1 1 0 0 0 1 0 1 0 0 1 1 1 0 1 1 1 1 0 1 1 0 1 0 0 0 0 1 0 0 0 1 0 0 1 1 0 1 1 0 0 1 1 0 0 1 0 1 0 1']

m = ['1 1 1 0 1 0 1 1 0 0 1 1 0 0 1 1 0 0 0 1 1 1 1 0 1 0 1 1 0 1 1 0 0 0 1 1 0 0 0 0 1 1 1 1 0 1 1 0 0 1 1 0 0 0 1 1 0 0 0 0 1',
'1 0 1 1 1 0 1 0 1 0 1 0 1 0 0 1 0 1 0 1 1 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0']
kPos = ['1 1 1 1 1']
sPos = ['1 1 1 1 1']
mPos = ['1 1']

key = k + s + m + kPos + sPos + mPos

print(lsz42("abc", key))
print(lsz42(lsz42("abc", key), key))

