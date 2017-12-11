def lsz40(plaintext, key, limitationSetting = "none"):
    # international telepgrah alphabet code
    ita2 = [24, 19, 14, 18, 16, 22, 11, 5, 12, 26, 30, 9, 7, 6, 3, 13, 29, 10, 20, 1, 28, 15, 25, 23, 21, 17, 2, 8, 31, 27, 4, 0, 4, 4, 31, 27]
    ltrs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ34-+9/ .85"

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

        chi2Back = chi[1][(chiPos[1] - 1) % len(chi[1])]
        # calculate the limitation
        basicMotor = motor[1][motorPos[1]]
        if limitationSetting == "chi2 one back":
            limitation = chi2Back
        else: limitation = True
        totalMotor = basicMotor or not limitation

        # advance chi wheels
        # the index will be decremented
        for i in range(5): chiPos[i] = (chiPos[i] + 1) % len(chi[i])

        # advance the motor wheels
        # m2
        if (motor[0][motorPos[0]]): motorPos[1] = (motorPos[1] + 1) % len(motor[1])
        # m1
        motorPos[0] = (motorPos[0] + 1) % len(motor[0])

        # advance the psi wheels
        if (totalMotor):
            for i in range(5):
                psiPos[i] = (psiPos[i] + 1) % len(psi[i])

        cipherText += ltrs[ita2.index(encryptedLetter)]

    return cipherText

key1 = ['01100111000011100111000010011011000110110', '0001100110001011110111000011011', '01111011000111000110001100100', '10100111010011000110010101', '10100001110100011110010', '0001110011100111100011000110011100011001011', '11010011100111001100011110001110011001110001000', '111001100011000111000100011110001001110011100110010', '10111001100011001001110011000100011110011100110011100', '01100010011100110011100110001111001001110011110001000111001', '1010101111010101110111011101101101101101110101011101110101101', '1110111011101011011101110110101101010']
chiPos1 = ['1 1 1 3 1']
psiPos1 = ['20 38 38 33 46']
motorPos1 = ['21 14']
key1 = key1 + chiPos1 + psiPos1 + motorPos1

chi2 = ['01111010110101100100110100001100001111000', '0111000010001101010001101110011', '11001101100111000010011011100', '11110010011001001101001100', '01110111000100110100010']
psi2 = ['0001110011101100101011011010010010101010100', '11010011100000111101001011001101010101010110100', '100100110111000111000011110101011001001010101010101', '01000010010111110110011001100001011010101010101100101', '10101001100110110010001000010110111101110010100011010101010']
motor2 = ['1000011000110011011110000110001101101011110001100110011010111', '0101010101010101110101001010101011101']
chiPos2 = ['3 11 16 18 7']
psiPos2 = ['9 27 17 22 25']
motorPos2 = ['21 11']
key2 = chi2 + psi2 + motor2 + chiPos2 + psiPos2 + motorPos2

key3 = ['00011110000110000101100100110101101011110', '1100111011000101011000100001110', '00111011001000011100110110011', '00110010110010011001001111', '01000101100100011101110', '0010101010100100101101101010011011100111000', '00101101010101010110011010010111100000111001011', '101010101010100100110101011110000111000111011001001', '10100110101010101011010000110011001101111101001000010', '01010101011000101001110111101101000010001001101100110010101', '1110101100110011000111101011011000110000111101100110001100001', '1011101010101001010111010101010101010', '0 6 7 3 4', '8 26 16 21 24', '20 10']

text2 = "JSKNWQTRJGICHZYJYVZTMX4HVAYWBEVVIJLM"
text2 = "QZAHLEN"

print(lsz40(text2, key3, "chi2 one back"))

