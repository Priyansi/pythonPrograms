def identityMatrix(rows, columns):

    for i in range(1, rows+1):
        for j in range(1, columns+1):
            identityMatrix[i-1][j-1] = (i/j)*(j/i)
    return identityMatrix


rows, columns = input().split(' ')
print(identityMatrix(rows, columns))
