def countTriangles(p):
    store = []
    if p % 2 != 0:
        return 0
    else:
        count = 0
        for b in range(1, p // 2):

            a = p / 2 * ((p - 2 * b) / (p - b))
            inta = int(a)
            if (a == inta):
                ab = tuple(sorted((inta, b)))
                if ab not in store:
                    count += 1
                    store.append(ab)
        return count


def peri():
    num = maxPeriCount = perimeter = 0
    for i in range(1, 1000):
        num = countTriangles(i)
        if num > maxPeriCount:
            perimeter = i
            maxPeriCount = num
    return perimeter


print(peri())
