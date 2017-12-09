def lsz42(plaintext):
    # international telepgrah alphabet code
    ltrs = 'E\nA SIU\rDRJNFCKTZLWHYPQOBG#MXV@'
    # fig = "3\n- '87\r~4^,!:(5+)2$6019?&#./;@"
    # ita2 = {'': 0}
    # ita2.update(dict(zip(ltr, range(1, 32))))
    # ita2.update(dict(zip(fig, range(1, 32))))
    
    # initialize all the cams on the wheels to 0
    # all wheels start at position 0
    # k / chi wheels
    k = [[False] * 41, [False] * 31, [False] * 29, [False] * 26, [False] * 23]
    k[0][0] = True
    kPos = [0,0,0,0,0]
    # s / psi wheels
    s = [[False] * 43, [False] * 47, [False] * 51, [False] * 53, [False] * 59]
    sPos = [0,0,0,0,0]
    # m / motor wheels
    m = [[False] * 61, [False] * 37]
    mPos = [0, 0]
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

print(lsz42("abc"))
print(lsz42(lsz42("abc")))


