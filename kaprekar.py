import sys


def num2digits(n: int) -> [int]:
    return [int(ch) for ch in str(n)]


def digits2num(ds: [int]) -> int:
    return int(''.join([str(i) for i in ds]))


def next(n: int) -> int:
    ds = num2digits(n)
    maxi = digits2num(sorted(ds, reverse=True))
    mini = digits2num(sorted(ds))
    return n, maxi, mini, maxi-mini


def kap_seq(n: int) -> [int]:
    nn = next(n)
    if nn[-1] == n:
        return [nn]
    return [nn]+kap_seq(nn[-1])


for k in kap_seq(int(sys.argv[1])):
    print(k)
