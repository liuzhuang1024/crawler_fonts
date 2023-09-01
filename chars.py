import string
import csv

# usualUniCode_3500 = \
#     [ord(i) for i in string.printable[:-1]] + \
#     [i for i in range(0x4e00, 0x9fff+1, 1)]

usualUniCode_3500 = \
    [ord(i) for i in string.printable[:-1]] + \
    [ord(i[1]) for i in csv.reader(open('7000通用汉字.csv'))]

