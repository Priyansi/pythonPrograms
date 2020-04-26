def SplitParenthesis(txt):
    brackets = []
    cluster = []
    for i, j in enumerate(txt):
        if j == '(':
            if len(brackets) == 0:
                start = i
            brackets.append('(')
        if j == ')':
            brackets.pop()
        if len(brackets) == 0:
            cluster.append(txt[start:i+1])
    return cluster


print(SplitParenthesis("((())())(()(()()))"))
