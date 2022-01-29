def work():
    x = 0
    def new_work():
        nonlocal x
        x += 3
        return x
    return new_work()

f = work
print(f())
print(f())
print(f())


def work_1():
    x = 0
    def new_work_1():
        nonlocal x
        x += 3
    new_work_1()
    print(x)

work_1();


def work_2():
    x = 0
    def new_work_2():
        nonlocal x
        x += 3
        return x
    return new_work_2

f = work_2();
""" f = new_work_2 """
""" work_2 is like a namespace """
print(f())
print(f())
print(f())

def ff(x):
    x = 4
    def g(y):
        def h(z):
            nonlocal x
            x = x + 1
            return x + y + z
        return h
    return g
a = ff(1)
b = a(2)
print(b(3) + b(4));
print(233)

def make_withdraw(balance):
    """Returns a function which can withdraw
    some amount from balance

    >>> withdraw = make_withdraw(50)
    >>> withdraw(25)
    25
    >>> withdraw(25)
    0
    """
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return "Insufficient funds"
        balance = balance - amount
        return balance
    return withdraw

withdraw = make_withdraw(50)
print(withdraw(25))
print(withdraw(25))

def tf(x):
    def tg(y):
        nonlocal x
        x += y
        return x + y
    return tg

print(tf(20)(25))
print(tf(20)(25))
th = tf(20);
print(th(25))
print(th(25))
