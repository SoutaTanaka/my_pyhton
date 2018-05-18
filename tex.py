for j in range(1,21):
    a = "&" + str(j)
    for i in range(1,16):
        a = a + "&"
        a = a + str((j**i)%33)
    a = a + "¥¥¥cline{2-17}"
    print(a)
