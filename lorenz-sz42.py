def lsz42()
    # international telepgrah alphabet code
    ltr = 'E\nA SIU\rDRJNFCKTZLWHYPQOBG#MXV@'
    fig = "3\n- '87\r~4^,!:(5+)2$6019?&#./;@"
    ita2 = {'': 0}
    ita2.update(dict(zip(ltr, range(1, 32))))
    ita2.update(dict(zip(fig, range(1, 32))))
    
    # initialize all the cams on the wheels to 0
    # k / chi wheels
    k1 = [False] * 41
    k2 = [False] * 31
    k3 = [False] * 29
    k4 = [False] * 26
    k5 = [False] * 23
    # s / psi wheels
    s1 = [False] * 43
    s2 = [False] * 47
    s3 = [False] * 51
    s4 = [False] * 53
    s5 = [False] * 59
    # m / motor wheels
    m1 = [False] * 61
    m2 = [False] * 37


    



