def findGcd(a, b):
    return a if b == 0 else findGcd(b, a % b)


allGcd = []
n = int(input())
if n != -1:
    _ = int(input())
    for i in range(n):
        line = list(map(int, input().split(' ')))
        for node in range(0, len(line)-1, 2):
            if line[node] != -1 and line[node+1] != -1:
                allGcd.append(findGcd(line[node], line[node+1]))

if allGcd:
    print(max(allGcd)-min(allGcd))
else:
    print(0)
