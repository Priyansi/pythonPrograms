def expand(num):
    digits = str(num)
    output = []
    for i, digit in enumerate(digits):
        if digit != '0':
            output.append(str(int(digit)*10**(len(digits)-i-1)))
    return " + ".join(output)


print(expand(5325))
