# Amir Shahbazi - 9812033

import numpy as np

# functions
# ---------------------------------------------------------


def func(x):
    f = x * np.cosh((6 / x) - np.arccosh(5 / x)) - 5
    return f


# ----------------------------------------------------------


def check(a, b):
    a1 = func(a)
    b1 = func(b)
    if ((a1 * b1) < 0) == False:
        return False
    else:
        return True


# -----------------------------------------------------------


def get_repetitions():

    m = int(input("Enter number of repetition: "))
    return m


# -----------------------------------------------------------


def false_position_method(a, b):
    if check(a, b) == True:
        n = get_repetitions()

        i = 0
        while i < n:

            x = (a * func(b) - b * func(a)) / (func(b) - func(a))

            if func(x) == 0:
                break
            else:
                if check(a, x) == True:
                    b = x

                elif check(x, b) == True:
                    a = x

            i += 1

        return x
    else:
        print("Invalid Input!")


# ---------------------------------------------------------


print("First root: {}".format(false_position_method(1, 2)))

print("Second root: {}".format(false_position_method(3, 4)))
