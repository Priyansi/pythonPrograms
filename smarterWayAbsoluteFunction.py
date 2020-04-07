def absoluteFunction(number):
    number -= (number < 0)*2*number
    return number


number = int(input())
print(absoluteFunction(number))
