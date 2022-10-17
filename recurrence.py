from fractions import Fraction

def recurrence(n):
    if n == 1:
        return 0
    if n == 2: 
        return 1

    else:
        return (1/n * recurrence(n-1) + 2/(n * (n-1)) * recurrence(n-2))


for i in range(1,10):
    print("a{} : {} a0".format(i, Fraction(recurrence(i)).limit_denominator()))

print("===")

def recurrence1(n):
    if n == 0:
        return 0
    if n == 1: 
        return 1

    else:
        return (1/n * recurrence1(n-1) + 2/(n * (n-1)) * recurrence1(n-2))


for i in range(1,10):
    print("a{} : {} a1".format(i, Fraction(recurrence1(i)).limit_denominator()))