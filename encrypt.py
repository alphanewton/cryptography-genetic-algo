import random as rand

def evenIndexStr(String: list):
    even = []
    for i in range(len(String)):
        if i % 2 == 0:
            even.append(String[i])
    print(f"Even: {even}")
    return even


def oddIndexStr(String: list):
    odd = []
    for i in range(len(String)):
        if i % 2 == 1:
            odd.append(String[i])
    print(f"Odd:  {odd}")
    return odd


def textToAscii(String: list):
    print("Inside textToascii()")
    for i in range(len(String)):
        String[i] = ord(String[i])
    print(String)


def AsciiToText(String: list):
    print("\n\nInside AsciiToText()")
    for i in range(len(String)):
        String[i] = chr(String[i])

    return String


def reSizer(String: list, k: int):
    print("\nInside reshaper()")
    p = 4 * k
    n = len(String)
    x = 0
    for i in range(n):
        if (n + i) % p == 0:
            x = i
            break
    print(f"Text re-size parameter is {x}")
    if x == 0:
        x = p
    for i in range(x):
        if i != x - 1:
            String.append(102 + i)
        else:
            String.append(127 - x)
    print(String)


def applyKey(String: list, Key: list):
    print("\nInside applyKey()")
    for i in range(len(String)):
        String[i] = String[i] ^ ord(Key[i % len(Key)])
    print(String)
    print()


def two_point_crossover(String1: list, String2: list):
    print("\nInside two_pointCrossover()")
    n = len(String1)
    for i in range(int(n / 4), int(n / 2)):
        String1[i], String2[i] = String2[i], String1[i]
    for i in range(int(3 * n / 4), n):
        String1[i], String2[i] = String2[i], String1[i]
    print(String1)
    print(String2)
    return String1, String2


def MatrixTranspose(String1: list, String2: list):
    print("\nInside MatrixOperations()")
    n = len(String1)
    d = 0
    for i in range(n):
        if (i * i) >= n:
            d = i
            break
    print(f"Matrix Dimensions are {d} x {d}")
    k = 0
    Mat1 = [[0 for i in range(d)] for j in range(d)]
    Mat2 = [[0 for i in range(d)] for j in range(d)]
    for i in range(d):
        for j in range(d):
            if k < n:
                Mat1[i][j] = String1[k]
                Mat2[i][j] = String2[k]
                k += 1
            elif k == n:
                Mat1[i][j] = 94
                Mat2[i][j] = 94
                k += 1
            else:
                Mat1[i][j] = rand.randint(10, 93)
                Mat2[i][j] = rand.randint(10, 93)

    print("\nMatrix_1:")
    for row in Mat1:
        print(row)
    print("------------------------\nMatrix_2:")
    for row in Mat2:
        print(row)
    print("------------------------")

    TMat1 = [[0 for i in range(d)] for j in range(d)]
    TMat2 = [[0 for i in range(d)] for j in range(d)]

    for i in range(d):
        for j in range(d):
            TMat1[i][j] = Mat1[j][i]
            TMat2[i][j] = Mat2[j][i]

    print("Transpose(Matrix_1):")
    for row in TMat1:
        print(row)
    print("------------------------\nTranspose(Matrix_2):")
    for row in TMat2:
        print(row)

    str_1 = []
    str_2 = []

    for i in range(d):
        for j in range(d):
            str_1.append(TMat1[i][j])
            str_2.append(TMat2[i][j])

    print(f"\nList(Matrix_1): {str_1}\nList(Matrix_2): {str_2}")
    return str_1, str_2


def Mutation(String1: list, String2: list, Key: list):
    print("\nInside Mutation()")
    n = len(String1)
    i = int(n / 2)
    String1[i] = String1[i] ^ ord(Key[i % len(Key)])
    String1[n - 2] = String1[n - 2] ^ ord(Key[(n - 2) % len(Key)])
    String2[i] = String2[i] ^ ord(Key[i % len(Key)])
    String2[n - 2] = String2[n - 2] ^ ord(Key[(n - 2) % len(Key)])
    print(f"{String1}\n{String2}")
    return String1, String2


def encrypt(Ptext: str, re_fac: int, Key: list):
    Text = list(Ptext)

    textToAscii(Text)
    reSizer(Text, re_fac)
    applyKey(Text, Key)
    L1, L2 = two_point_crossover(evenIndexStr(Text), oddIndexStr(Text))
    L1, L2 = MatrixTranspose(L1, L2)
    L1, L2 = Mutation(L1, L2, Key)
    L1.extend(L2)
    cipher = AsciiToText(L1)
    print(f"Cipher Text in List Format:\n{cipher}")

    msg = ""
    for i in cipher:
        msg += i
    return msg
