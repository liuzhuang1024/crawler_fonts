import string
usualUniCode_3500 = \
    [ord(i) for i in string.printable[:-1]] + \
    [i for i in range(0x4e00, 0x9fff+1, 1)]