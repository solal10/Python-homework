import random
from random import randint


class Euro:
    def __init__(self, amount):
        """
        constructor of the euro class
        :param amount:how many euro
        """
        self.__amount = amount

    def amount(self):
        """
        :return: return the amount of euro in shekel
        """
        return rates['euro', 'nis'] * self.__amount

    def __add__(self, second):
        """
        operator overloading of the operator +
        :param second: the money you want to add
        :return: the addition of the two value
        """
        return self.amount() + second.amount()

    def getamount(self):
        """
        get the amount of euro saved in the object
        :return: the amount of the object
        """
        return self.__amount

    def __str__(self):
        """
        :return: return the format for the printing of the object
        """
        return f'Euro:{self.__amount}'

    def __repr__(self):
        """
        :return: format for the repr function
        """
        return f'Euro:{self.__amount}'


class Dollar:
    def __init__(self, amount):
        """
        constructor of the dollar class
        :param amount: amount of dollar in the object
        """
        self.__amount = amount

    def amount(self):
        """
        :return: the amount of dollar in shekel of the object
        """
        return rates['dollar', 'nis'] * self.__amount

    def __add__(self, second):
        """
        operator overloading of the + operator
        :param second: second object
        :return: the addition of the two object in shekel
        """
        return self.amount() + second.amount()

    def getamount(self):
        """
        :return: amount value of the object
        """
        return self.__amount

    def __str__(self):
        """
        :return: format to print the object
        """
        return f'Dollar:{self.__amount}'

    def __repr__(self):
        """
        :return: format for the repr function
        """
        return f'Dollar:{self.__amount}'


class Shekel:
    def __init__(self, amount):
        """
        constructor of the shekel class
        :param amount: amount of shekel in the object
        """
        self.__amount = amount

    def amount(self):
        """
        return the amount of shekel in the object
        :return: amount
        """
        return self.__amount

    def __add__(self, second):
        """
        operator overloading of the operator +
        :param second: second object to add
        :return: addition of the two object in shekel
        """
        return self.amount() + second.amount()

    def getamount(self):
        """
        get function
        :return: amount of the object
        """
        return self.__amount

    def __str__(self):
        """
        :return: format to print
        """
        return f'Shekel:{self.__amount}'

    def __repr__(self):
        """
        :return: format for the repr function
        """
        return f'Shekel:{self.__amount}'


def add(x, y):
    return x + y


def type_tag(x):
    """
    :param x: an object
    :return: the type of the object that we find in the dictionnary
    """
    return type_tag.tags[type(x)]


def add1(x1, x2):
    """
    :param x1: object 1
    :param x2: object 2
    :return: the additions of both object after looking what is the add fucnction to use in the dictionary
    """
    types = (type_tag(x1), type_tag(x2))
    return add.implementations[types](x1, x2)


def sub(x1, x2):
    """

    :param x1: object 1
    :param x2: object2
    :return: the substactions of both object after looking what is the add fucnction to use in the dictionary
    """
    types = (type_tag(x1), type_tag(x2))
    return sub.implementations[types](x1, x2)


def add_euro_euro(x1, x2):
    """
    :param x1: object euro
    :param x2: object euro
    :return: addition of the objects
    """
    temp = x1.getamount() + x2.getamount()
    return type(x1)(temp)


def add_dollar_dollar(x1, x2):
    """
    :param x1: dollar object
    :param x2: object
    :return: addtion of the objects
    """
    temp = x1.getamount() + x2.getamount()
    return type(x1)(temp)


def add_shekel_shekel(x1, x2):
    """
    :param x1: shekel object
    :param x2: shekel object
    :return: addition of the objects
    """
    temp = x1.getamount() + x2.getamount()
    return type(x1)(temp)


def add_euro_dollar(x1, x2):
    """
    :param x1: euro object
    :param x2: dollar object
    :return: addition of the objects return an object of type euro
    """
    temp = x1.getamount() + (rates['dollar', 'euro'] * x2.getamount())
    return type(x1)(temp)


def add_euro_shekel(x1, x2):
    """
    :param x1: euro object
    :param x2: shekel object
    :return: addition of the objects return a euro object
    """
    temp = x1.getamount() + (rates['nis', 'euro'] * x2.getamount())
    return type(x1)(temp)


def add_dollar_shekel(x1, x2):
    """
    :param x1: dollar object
    :param x2: shekel object
    :return: addition of the objects return a dollar object
    """
    temp = x1.getamount() + (rates['nis', 'dollar'] * x2.getamount())
    return type(x1)(temp)


def add_dollar_euro(x1, x2):
    """
     :param x1: dollar object
     :param x2: euro object
     :return: addition of the objects return a dollar object
     """
    temp = x1.getamount() + (rates['euro', 'dollar'] * x2.getamount())
    return type(x1)(temp)


def add_shekel_euro(x1, x2):
    """
     :param x1: shekel object
     :param x2: euro object
     :return: addition of the objects return a shekel object
     """
    temp = x1.getamount() + (rates['euro', 'nis'] * x2.getamount())
    return type(x1)(temp)


def add_shekel_dollar(x1, x2):
    """
     :param x1: shekel object
     :param x2: dollar object
     :return: addition of the objects return a shekel object
     """
    temp = x1.getamount() + (rates['dollar', 'nis'] * x2.getamount())
    return type(x1)(temp)


def sub_euro_euro(x1, x2):
    """
     :param x1: euro object
     :param x2: euro object
     :return: substactions of the objects return a euro object
     """
    temp = x1.getamount() - x2.getamount()
    return type(x1)(temp)


def sub_dollar_dollar(x1, x2):
    """
     :param x1: dollar object
     :param x2: dollar object
     :return: substactions of the objects return a dollar object
     """
    temp = x1.getamount() - x2.getamount()
    return type(x1)(temp)


def sub_shekel_shekel(x1, x2):
    """
     :param x1: shekel object
     :param x2: shekel object
     :return: substactions of the objects return a shekel object
     """
    temp = x1.getamount() - x2.getamount()
    return type(x1)(temp)


def sub_euro_dollar(x1, x2):
    """
     :param x1: euro object
     :param x2: dollar object
     :return: substactions of the objects return a euro object
     """
    temp = x1.getamount() - (rates['dollar', 'euro'] * x2.getamount())
    return type(x1)(temp)


def sub_euro_shekel(x1, x2):
    """
     :param x1: euro object
     :param x2: shekel object
     :return: substactions of the objects return a euro object
     """
    temp = x1.getamount() - (rates['nis', 'euro'] * x2.getamount())
    return type(x1)(temp)


def sub_dollar_shekel(x1, x2):
    """
     :param x1: dollar object
     :param x2: shekel object
     :return: substactions of the objects return a dollar object
     """
    temp = x1.getamount() - (rates['nis', 'dollar'] * x2.getamount())
    return type(x1)(temp)


def sub_dollar_euro(x1, x2):
    """
     :param x1: dollar object
     :param x2: euro object
     :return: substactions of the objects return a dollar object
     """
    temp = x1.getamount() - (rates['euro', 'dollar'] * x2.getamount())
    return type(x1)(temp)


def sub_shekel_euro(x1, x2):
    """
     :param x1: shekel object
     :param x2: euro object
     :return: substactions of the objects return a shekel object
     """
    temp = x1.getamount() - (rates['euro', 'nis'] * x2.getamount())
    return type(x1)(temp)


def sub_shekel_dollar(x1, x2):
    """
     :param x1: shekel object
     :param x2: dollar object
     :return: substactions of the objects return a shekel object
     """
    temp = x1.getamount() - (rates['dollar', 'nis'] * x2.getamount())
    return type(x1)(temp)


def apply(x, y, z):
    """
    :param x: actions(add or sub)
    :param y: currency object
    :param z: currency object
    :return: return the addtion of both the object
    """
    return apply.implementations[x](y, z)


def dollar_to_shekel(x):
    """
    :param x: dollar object
    :return: return a shekel object after conversion
    """
    return Shekel(rates['dollar', 'nis'] * x.getamount())


def euro_to_shekel(x):
    """
    :param x: euro object
    :return: a shekl object after conversion
    """
    return Shekel(rates['euro', 'nis'] * x.getamount())


def coerce_apply(operator_name, x, y):
    """

    :param operator_name: sub or add
    :param x: currency object
    :param y: currency object
    :return: the addition/substractions of the two objects after conversions of them
    """
    tx, ty = type_tag(x), type_tag(y)
    if tx != 'Shekel':
        x = coercions[(tx, 'nis')](x)
    if ty != 'Shekel':
        y = coercions[(ty, 'nis')](y)
    return coerce_apply.implementations[operator_name](x, y)


def add2(x, y):
    """
    :param x: shekel object
    :param y: shekel object
    :return: an object of shekel type after addition of both object
    """
    return Shekel(x.getamount() + y.getamount())


def sub2(x, y):
    """
    :param x: shekel object
    :param y: shekel object
    :return: an object of shekel type after substraction of both object
    """
    return Shekel(x.getamount() - y.getamount())


rates = {('dollar', 'nis'): 3.82, ('euro', 'nis'): 4.07, ('euro', 'dollar'): 1.06}
type_tag.tags = {Euro: 'Euro', Shekel: 'Shekel', Dollar: 'Dollar'}
add.implementations = {('Euro', 'Euro'): add_euro_euro, ('Dollar', 'Dollar'): add_dollar_dollar,
                       ('Shekel', 'Shekel'): add_shekel_shekel, ('Euro', 'Dollar'): add_euro_dollar, ('Euro', 'Shekel')
                       : add_euro_shekel, ('Dollar', 'Shekel'): add_dollar_shekel,
                       ('Dollar', 'Euro'): add_dollar_euro, ('Shekel', 'Euro'): add_shekel_euro,
                       ('Shekel', 'Dollar'): add_shekel_dollar}
sub.implementations = {('Euro', 'Euro'): sub_euro_euro, ('Dollar', 'Dollar'): sub_dollar_dollar,
                       ('Shekel', 'Shekel'): sub_shekel_shekel, ('Euro', 'Dollar'): sub_euro_dollar, ('Euro', 'Shekel')
                       : sub_euro_shekel, ('Dollar', 'Shekel'): sub_dollar_shekel,
                       ('Dollar', 'Euro'): sub_dollar_euro, ('Shekel', 'Euro'): sub_shekel_euro,
                       ('Shekel', 'Dollar'): sub_shekel_dollar}
apply.implementations = {'add': add1, 'sub': sub}
coercions = {('Dollar', 'nis'): dollar_to_shekel, ('Euro', 'nis'): euro_to_shekel}
coerce_apply.implementations = {'add': add2, 'sub': sub2}


class N_arry:
    def __init__(self, entry):
        """
        constructor of the the tree
        :param entry: root of the tr
        """
        self.node = (entry, [None, None, None, None])

    def addtotree(self, newentry):
        """
        add a value to the tree via a recursion
        :param newentry: the value you want to add
        :return: dont return a value
        """
        if newentry <= self.node[0]:
            if self.node[1][0] == None:
                self.node[1][0] = N_arry(newentry)
            elif self.node[1][1] == None:
                self.node[1][1] = N_arry(newentry)
            else:
                k = random.randint(0, 1)
                self.node[1][k].addtotree(newentry)
        if newentry > self.node[0]:
            if self.node[1][2] == None:
                self.node[1][2] = N_arry(newentry)
            elif self.node[1][3] == None:
                self.node[1][3] = N_arry(newentry)
            else:
                k = random.randint(2, 3)
                self.node[1][k].addtotree(newentry)

    def intree(self, value):
        """
        check if the value is in the tree
        :param value: the value you want to check
        :return: 1 if the value is not in the tree
        0 if the value is in the tree
        """
        x = 1
        if value == self.node[0]:
            return 0
        if value != self.node[0] and self.node[1] == [None, None, None, None]:
            return 1
        else:
            if value > self.node[0]:
                if self.node[1][2] != None:
                    x = self.node[1][2].intree(value)
                if self.node[1][3] != None:
                    x = self.node[1][3].intree(value)
            if value < self.node[0]:
                if self.node[1][0] != None:
                    x = self.node[1][0].intree(value)
                if self.node[1][1] != None:
                    x = self.node[1][1].intree(value)
        return x

    def deletefromtree(self, value):
        """
        delete a value from the tree
        :param value: the value you want to delete from the tree
        :return: nothing
        """
        if self.node[0] == value and self.node[1] == [None, None, None, None]:
            return 'found'
        elif self.node[0] == value and self.node[1] != [None, None, None, None]:
            raise TreeIllegalValue(value)
        if self.node[0] != value and self.node[1] == [None, None, None, None]:
            return 'no'
        if value > self.node[0]:
            if self.node[1][2] != None:
                x = self.node[1][2].deletefromtree(value)
                if x == 'found':
                    self.node[1][2] = None
                    return 'done'
                if x == 'done':
                    return 'done'
                if x == 'no':
                    return 'no'
            if self.node[1][3] != None:
                x = self.node[1][3].deletefromtree(value)
                if x == 'found':
                    self.node[1][3] = None
                    return 'done'
                if x == 'done':
                    return 'done'
                if x == 'no':
                    return 'no'
        if value < self.node[0]:
            if self.node[1][0] != None:
                x = self.node[1][0].deletefromtree(value)
                if x == 'found':
                    self.node[1][0] = None
                    return 'done'
                if x == 'done':
                    return 'done'
                if x == 'no':
                    return 'no'
            if self.node[1][1] != None:
                x = self.node[1][1].deletefromtree(value)
                if x == 'found':
                    self.node[1][1] = None
                    return 'done'
                if x == 'done':
                    return 'done'
                if x == 'no':
                    return 'no'

    def __str__(self):
        """
        :return:format to print the tree via recursive function
        """
        if self.node[1] == [None, None, None, None]:
            return f'{self.node[0]}[None,None,None,None]'
        else:
            return f'{self.node[0]},[{self.node[1][0].__str__(), self.node[1][1].__str__(), self.node[1][2].__str__(), self.node[1][3].__str__()}]'

    def __str__(self):
        """
        :return:format for the repr function
        """
        if self.node[1] == [None, None, None, None]:
            return f'N_arry {self.node[0]}[None,None,None,None]'
        else:
            return f'N_arry {self.node[0]},[{self.node[1][0].__str__(), self.node[1][1].__str__(), self.node[1][2].__str__(), self.node[1][3].__str__()}]'


class TreeError(Exception):
    def __init__(self, value):
        """
        constructor of the class treeerror which inheritate of the exception class which is built in the pyhton language
        :param value: the value that cause the exception
        """
        self.value = value


class TreeValueDoesNotExist(TreeError):
    def __str__(self):
        """
        :return: format to print the exception
        """
        return f'TreeValueDoesNotexist : {self.value}'

    def __repr__(self):
        """
        :return:format for the repr function
        """
        return f'TreeValueDoesNotexist : {self.value}'


class TreeIllegalValue(TreeError):
    def __str__(self):
        """
        :return: format to print the exception
        """
        return f'TreeIllegalValue : {self.value}'

    def __repr__(self):
        """
        :return:format for the repr function
        """
        return f'TreeIllegalValue : {self.value}'


try:
    tree = None
    i = 0
    while i != 5:
        i = input('1)build a tree \n2)add value to tree \n3)delete value in tree \n4)print tree 5) end of the program\n')
        i=int(i)
        if i == 1:
            value = input('enter value\n')
            tree = N_arry(value)
        if i == 2:
            value = input('enter the value you wish to add to the tree\n')
            try:
                tree.addtotree(value)
            except UnboundLocalError:
                print('tree does not exist yet\n')
        if i == 3:
            value = input('enter the value you wish to delete from the tree\n')
            try:
                temp = tree.intree(value)
                if temp == 1:
                    raise TreeValueDoesNotExist(value)
                tree.deletefromtree(value)
            except UnboundLocalError:
                print('tree does not exist yet\n')
            except TreeError as x:
                print(x)
        if i == 4:
            print(tree)
        if i ==5 :
            print('thank you goodbye\n')
except:
    print('error end of program')