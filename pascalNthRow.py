import math
import sys


def pascalNthRow(row):
    return ' '.join(str(math.factorial(row)//(math.factorial(i)*math.factorial(row-i))) for i in range(row+1))


print(pascalNthRow(int(sys.argv[1])))
