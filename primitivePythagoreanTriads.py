import math


def primitive_pyth() -> [(int, int, int)]:
    triadList = []
    for m in range(1, 100):
        for n in range(m+1, 101):
            if m**2+n**2 > 100:
                break
            if (m & 1 and n & 1) or math.gcd(m, n) != 1:
                continue
            a = n**2 - m**2
            b = 2*m*n
            c = m**2+n**2
            if b > a:
                triadList.append((a, b, c))
            else:
                triadList.append((b, a, c))
    return sorted(triadList)


print(primitive_pyth())


print(primitive_pyth())
