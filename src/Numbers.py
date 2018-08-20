import math

def simple_math():
    print("\n****** Simple Math Operations ******")
    print("2 + 2            = ", 2 + 2)                     # sum
    print("2 - 1            = ", 2 - 1)                     # minus
    print("3 * 3            = ", 3 * 3)                     # multyply
    print("5 / 2            = ", 10 / 2)                    # division, by default returns floating point value
    print("int(5 / 2)       = ", int(10 / 2))               # division, by default returns floating point value
    print("7 % 4            = ", 7 % 4)                     # mod (returns the reminder from the division)
    print("2 ^ 3            = ", 2 ** 3)                    # exponent
    print("(2 + 3) * 4      = ", (2 + 3) * 4)               # first execute what is in the brackets

def floating_points():

    # If you like more precise working with floating points, it will be useful to use `decimal` and `fractions` modules.
    # In a case you need heavy usage of operations with floating points, check SciPy project (https://scipy.org)

    print("\n****** Floating Points Operations ******")
    print("0.1 + 0.1        = ", 0.1 + 0.1)                 # sum of floating points
    print("0.5 - 0.2        = ", 0.5 - 0.2)                 # minus of floating points
    print(".1 + .1          = ", .1 + .1)                   # another valid representation of floating points
    print(".1 + .1 + .1     = ", .1 + .1 + .1)              # the things are getting complicated because of the approximation of storing the floating points
    print("0.1 + 0.2 - 0.3  = ", 0.1 + 0.2 - 0.3)           # the things are even more complicated. Most decimal fractions cannot be represented exactly as binary fractions
    print("PI with 12g      = ", format(math.pi, '.12g'))   # get only 12 significant digits from PI number
    print("PI with 2f       = ", format(math.pi, '.2f'))    # get PI number with only 2 digits after the point
    print("repr(PI)         = ", repr(math.pi))             # representation of the PI by 17 digits as a string. `repr()` function has printable representation of an object. repr(math.pi) + 2.0 will not work
    print("round(.1, 10) + round(.1, 10) + round(.1, 10) == round(.3, 10)   | Result = ", round(.1, 10) + round(.1, 10) + round(.1, 10) == round(.3, 10))   # floating point limitations
    print("round(.1 + .1 + .1, 10) == round(.3, 10)                         | Result = ", round(.1 + .1 + .1, 10) == round(.3, 10))                         # round function can help on this level
    print("Floating point number representation: %s " % (3.1415e-10))                                                                                       # exponential representation of the floating numbers



def advanced():
    print("\n****** Advanced Numbers ******")

    x = 0o10        # Octal System
    print("Octal (base 8) 0o10 = ", x)

    y = 0xA0F
    print("Hexadecimal (base 16) 0xA0F = ", y)

    z = 0b10110101
    print("Binary (base 2) 0b10110101 = ", z)

    print("Convert 65 into binary bin(65)       = ", bin(65))                                               # convert number in binary system
    print("Convert 65 into octal oct(65)        = ", oct(65))                                               # convert number in octal system
    print("Convert 65 into hexadecimal hex(65)  = ", hex(65))                                               # convert number in hexadecimal system

    k = 123123123432158923645781235478123654
    print("Integer is of unlimited size k = %s\n%s * %s * %s = %s" % (k, k, k, k, k * k * k))               # integer in python 3 has unlimited zise

    i = 3
    p = 2j
    print("Complex number format: <real part> + <imaginary part>j\ncomplex number = %s" % (i + p))

    div_x = 9
    div_y = 3
    print("Floot division %s // %s      = %s" % (div_x, div_y, div_x // div_y))

    div_x = 10
    div_y = 3
    print("Floot division %s // %s      = %s" % (div_x, div_y, div_x // div_y))

    div_x = 11
    div_y = 3
    print("Floot division %s // %s      = %s" % (div_x, div_y, div_x // div_y))

    div_x = 12
    div_y = 3
    print("Floot division %s // %s      = %s" % (div_x, div_y, div_x // div_y))

    div_x = 10.0
    div_y = 3
    print("Floot division %s // %s      = %s" % (div_x, div_y, div_x // div_y))

    div_x = -7
    div_y = 3
    print("Floot division %s // %s      = %s" % (div_x, div_y, div_x // div_y))


def main():
    # simple_math()
    # floating_points()
    advanced()

if __name__ == '__main__':
    main()
