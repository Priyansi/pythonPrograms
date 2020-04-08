import sys

equalTos = '==========='


def table(a, b):
    return ''.join(str(a)+' '+str(b))+''.join(' +\n' if a & 1 else '\n')


def russianMultiplication(a, b):
    outputString = ''
    total = 0
    indent = len(str(a))+1
    while a > 0:
        outputString += table(a, b)
        if outputString.endswith('+\n'):
            total += b
        a = a//2
        b = 2*b

    return outputString+equalTos+'\n'+(' '*indent)+str(total)+'\n'+equalTos


print(russianMultiplication(int(sys.argv[1]), int(sys.argv[2])))
