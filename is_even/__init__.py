__version__ = "1.0.2"

def isEven(n):
    res = [True, False]
    while True:
        try:
            return res[n]
        except IndexError:
            res += res
