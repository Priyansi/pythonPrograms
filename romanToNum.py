ROMAN = dict(zip(('MDCLXVI'), (1000, 500, 100, 50, 10, 5, 1)))


def romanToNum(s):
    num = 0
    s = s.replace('CM', 'DCCCC').replace('CD', 'CCCC').replace('XC', 'LXXXX').replace(
        'XL', 'XXXX').replace('IX', 'VIIII').replace('IV', 'IIII')
    return sum(ROMAN[ch] for ch in s)


print(romanToNum('MCMIV'))
