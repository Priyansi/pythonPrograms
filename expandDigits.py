def look_and_say(n):
    s = str(n)
    if len(s) & 1:
        return 'invalid'
    return int(''.join(int(s[i])*s[i+1] for i in range(0, len(s)-1, 2) if s[i] != '0'))


k = look_and_say(3132)
print(type(k))
