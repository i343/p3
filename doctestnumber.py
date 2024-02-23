from doctest import testmod

def Plas(f1 : int, f2: int) -> int:
    """Вернёт сумму двух чисел.

    >>> Plas(0, 2)
    2
    >>> Plas(1, 2)
    3
    >>> Plas(3, 5)
    9
    """

    return f1 + f2



if __name__ == "__main__":
    print(Plas(10,15))
    
    testmod()
    