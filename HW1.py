

def factorSum(x):
    """
    this function find the list of the prime number that divides the number x and then enter them in a list to return
    the sum of the list
    :param x: integer number super to 2
    :return: the sum of all prime number(only once) that divides the number x
    """
    divider = 2
    listof = set()
    while x != 1:
        if x % divider == 0:
            listof.add(divider)
            x = x / divider
        else:
            divider += 1
    return sum(listof)


def onlyPositive(f):
    """
    this function will cal define a function named func that call the function f with the absolute value of x
    :param f:it is a function that makes a cetrtain action over a number she receives
    :return: return a function of name func
    """
    def func(x):
        if x > 0:
            return f(x)
        else:
            return f(-x)
    return func


def f1(x):
    return x+1


def interceptPoint(x, y):
    """
    this function calculate the intersction point between two lines that the function receives if the lines are the same
    or are parralels then the function returns none
    otherwise we use the formula
    :param x: tuple that refers to a line name x (mX+p) m and p being the first and last value of the tuple
    :param y: tuple that refers to a line name y (mX+p) m and p being the first and last value of the tuple
    :return: it returns two value z and p that define the coordinates of the intersection point of the rights
    """
    if x[0] == y[0]:
        return "None"
    else:
        z = (y[1]-x[1])/(x[0]-y[0])
        p = x[0]*z+x[1]
        return z, p


def printNumbers(a, b, c):
    """
    this function prints the integer number from a to b and if the number c is between the numbers we dont print it
    :param a:integer
    :param b:integer
    :param c:integer
    """
    if a == b:
        print(b)
    elif a < b and a != c:
        print(a)
        printNumbers(a + 1, b, c)
    elif a == c and a < b:
        printNumbers(a + 1, b, c)
    elif a > b and a != c:
        print(a)
        printNumbers(a - 1, b, c)
    elif a == c and a > b:
        printNumbers(a - 1, b, c)


def arrProduct(a, b):
    """
    this function enters in a third array the value of the numbers in the a array numbers of time the integers in the b
    array at the same index equals to.
    :param a: array of integers
    :param b: array of integers
    :return: array of integers
    """
    c = []
    for i in range(len(a)):
        for y in range(b[i]):
            c.append(a[i])
    return c


def analyze(a):
    """
    the function turns the string into an array and removes the , and the space than with a loop we run through the
    array and check the number of time the temperature was above 75
    :param a: string of temperature separate by a , and a space
    :return: number of time the temperature was above 75
    """
    count = 0
    a = a.replace(",", "")
    arr = a.split(' ')
    longueur = len(arr)
    for i in range(longueur):
        if float(arr[i]) > 75.0:
            count = count + 1
    return count


print(factorSum(2520))
g = onlyPositive(f1)
print(g(-2))
print(interceptPoint((3, 11), (5, 1)))
printNumbers(2, -3, -1)
print(arrProduct([1, 2, 3], [0, 1, 2]))
print(analyze("96, 52.02, 67.3, 86.2, 87.1, 100"))
