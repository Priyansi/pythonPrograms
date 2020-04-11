import sys


def compressString(s):
    string = ''
    count = 0
    for i in range(len(s)-1):
        if s[i+1] == s[i]:
            count += 1
        else:
            if count > 1:
                string += str(count+1)+s[i]
            else:
                string += s[i]*(count+1)
            count = 0

    return string+str(count+1)+s[i+1] if count > 1 else string+s[i+1]*(count+1)


print(compressString(sys.argv[1]))
