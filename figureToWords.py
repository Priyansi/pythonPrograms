singleDigit = ['zero', 'one', 'two', 'three',
               'four', 'five', 'six', 'seven', 'eight', 'nine']
doubleDigit = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
               'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tenMultiple = ['', '', 'twenty', 'thirty', 'forty',
               'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
tenPower = 'hundred'


def fig2words(n: int) -> str:
    length = len(str(n))
    s = ''
    if length == 1:
        return singleDigit[n].capitalize()
    if length == 3:
        s += singleDigit[n//100]+' '+tenPower
        n = n % 100
        if n == 0:
            return s.capitalize()
        else:
            s += ' and '
    if n > 9 and n < 20:
        return (s+doubleDigit[n % 10]).capitalize()
    s += tenMultiple[n//10]
    return s.capitalize() if n % 10 == 0 else (s+' '+singleDigit[n % 10]).capitalize()


print(fig2words(50))
