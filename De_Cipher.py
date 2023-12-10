import math


def textToAscii(String: list):
    print("\nInside textToascii()")
    for i in range(len(String)):
        String[i] = ord(String[i])
    print(String)


def AsciiToText(String: list):
    print("\n\nInside AsciiToText()")
    for i in range(len(String)):
        String[i] = chr(String[i])

    return String


def applyKey(String: list, Key: list):
    print("\nInside applyKey()")
    for i in range(len(String)):
        String[i] = String[i] ^ ord(Key[i % len(Key)])
    print(String)


def Slicing(String1: list, String2: list):
    print("\nAfter Slicing:")
    s = 0
    for i in range(len(String1)-1, 0, -1):
        if String1[i] == 94:
            s = i
            break
    if s != 0:
        String1 = String1[0:s]
        String2 = String2[0:s]

    return String1, String2


def odd_evenMerge(String1: list, String2: list):
    print("\nInside odd_evenMerge()")
    L = []
    for i in range(0, len(String1)):
        L.append(String1[i])
        L.append(String2[i])

    print(L)
    return L


def Mutation(String1: list, String2: list, Key: list):
    print("\nInside Mutation()")
    n = len(String1)
    i = int(n/2)
    String1[i] = String1[i] ^ ord(Key[i % len(Key)])
    String1[n - 2] = String1[n - 2] ^ ord(Key[(n - 2) % len(Key)])
    String2[i] = String2[i] ^ ord(Key[i % len(Key)])
    String2[n - 2] = String2[n - 2] ^ ord(Key[(n - 2) % len(Key)])
    print(String1)
    print(String2)
    return String1, String2


def MatrixTranspose(String1: list, String2: list):
    print("\nInside MatrixOperations()")
    n = len(String1)
    d = int(math.sqrt(n))
    print(f"Matrix Dimensions are {d} x {d}")
    Mat1 = [[0 for i in range(d)] for j in range(d)]
    Mat2 = [[0 for i in range(d)] for j in range(d)]
    k = 0
    for i in range(d):
        for j in range(d):
            Mat1[i][j] = String1[k]
            Mat2[i][j] = String2[k]
            k += 1

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
    str_1, str_2 = Slicing(str_1, str_2)
    print(f"List(Matrix_1): {str_1}\nList(Matrix_2): {str_2}")
    return str_1, str_2


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


def decrypt(Ctext: str, Key: list):
    C_text = list(Ctext)
    print(f"Acquired Cipher Text is:\n{Ctext}")
    textToAscii(C_text)
    L1, L2 = C_text[0:int(len(C_text) / 2)], C_text[int(len(C_text) / 2):]
    L1, L2 = Mutation(L1, L2, Key)
    L1, L2 = MatrixTranspose(L1, L2)
    L1, L2 = two_point_crossover(L1, L2)
    Text = odd_evenMerge(L1, L2)
    applyKey(Text, Key)

    print("\nSlicing the Text to Original Length:")
    Text = Text[0:(len(Text) - (127 - Text[-1]))]
    print(Text)

    Text = AsciiToText(Text)
    print(f"Plain Text in List format:\n{Text}")

    msg = ""
    for i in Text:
        msg += i
    return msg
