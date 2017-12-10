def lsz40(plaintext, key, limitationSetting = "none"):
    # international telepgrah alphabet code
    ita2 = [24, 19, 14, 18, 16, 22, 11, 5, 12, 26, 30, 9, 7, 6, 3, 13, 29, 10, 20, 1, 28, 15, 25, 23, 21, 17, 2, 8, 31, 4, 27, 0]
    ltrs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ34-.+/9 85"

    boolify = lambda x: list(map(lambda c: bool(int(c)), x))
    chi = list(map(boolify, key[:5]))
    psi = list(map(boolify, key[5:10]))
    motor = list(map(boolify, key[10:12]))

    intify = lambda x: list(map(int, x))
    chiPos = intify(key[12].split(' '))
    psiPos = intify(key[13].split(' '))
    motorPos = intify(key[14].split(' '))

    cipherText = ''
    plaintext = plaintext.upper()
    for letter in plaintext:
        # each of the chi wheels operates on a single bit of the plaintext
        # for the sake of simplicity, treat the chi and psi wheels as 2 binary numbers
        chiCode = psiCode = 0
        for i in range(5):
            chiCode = (chiCode << 1) + chi[i][chiPos[i]]
            psiCode = (psiCode << 1) + psi[i][psiPos[i]]

        # first XOR the letter with the chi wheels, then with the psi wheels
        letterCode = ita2[ltrs.index(letter)]
        encryptedLetter = letterCode ^ chiCode ^ psiCode

        limitation = True
        if limitationSetting == "none": limitation = True
        elif limitationSetting == "chi2 one back":
            limitation = chi[1][(chiPos[1] - 1) % len(chi[1])]
        elif limitationSetting == "psi1":
            limitation = chi[1][(chiPos[1] - 1) % len(chi[1])]
            limitation ^= psi[0][(psiPos[0] - 1) % len(psi[0])]

        # turn the wheels
        if (motor[1][motorPos[1]] or not limitation):
            for i in range(5):
                psiPos[i] = (psiPos[i] + 1) % len(psi[i])

        if (motor[0][motorPos[0]]):
            motorPos[1] = (motorPos[1] + 1) % len(motor[1])

        motorPos[0] = (motorPos[0] + 1) % len(motor[0])

        for i in range(5):
            chiPos[i] = (chiPos[i] + 1) % len(chi[i])

        cipherText += ltrs[ita2.index(encryptedLetter)]

    return cipherText

key1 = ['01100111000011100111000010011011000110110', '0001100110001011110111000011011', '01111011000111000110001100100', '10100111010011000110010101', '10100001110100011110010', '0001110011100111100011000110011100011001011', '11010011100111001100011110001110011001110001000', '111001100011000111000100011110001001110011100110010', '10111001100011001001110011000100011110011100110011100', '01100010011100110011100110001111001001110011110001000111001', '1010101111010101110111011101101101101101110101011101110101101', '1110111011101011011101110110101101010']
chiPos1 = ['1 1 1 3 1']
psiPos1 = ['20 38 38 33 46']
motorPos1 = ['21 14']
key1 = key1 + chiPos1 + psiPos1 + motorPos1
text1 = "HELLO.WORLD"
text1 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
print(lsz40(text1, key1, "k2 one back"))

