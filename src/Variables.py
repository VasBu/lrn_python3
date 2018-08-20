def basics():
    print("\n****** Create and Delete Variables ******")
    x = 42                                                      # assigning integer variable
    print("x            = ", x)
    print("id(x)        = ", id(x))                             # get reference (identifier) of the variable

    y = x                                                       # assign variable to another
    print("y = x")
    print("y            = ", y)
    print("id(x), id(y) = (%s, %s)" % (id(x), id(y)))           # they are referencing to a same memory location

    y = 66                                                      # assign a new value for one of the values
    print("y            = ", y)
    print("id(x), id(y) = (%s, %s)" % (id(x), id(y)))           # the Python creates new memory location for the changed variable

    try:
        del y  # delete variable
        print("y            =", y)
    except Exception as e:
        print("[Error]", e)

def advanced():
    print("\n****** Advanced Working with Variables ******")

    x = 2
    y = "Vasil Buraliev"
    z = .5

    print('Detect type of a variable with `type` keyword\n x = %s(%s)\n y = %s(%s)\n z = %s(%s)' % (x, type(x), y, type(y), z, type(z)))

    a = b = c = 1
    print("Multiple assignment. a = b = c = %s" % (a))

    a,b,c = 1,2,"Vasil"
    print("Another way of assignment variables a,b,c = %s,%s,%s" % (a, b, c))

def global_local_variables_helper():
    global s
    print(s)
    s = "I love Paris!"
    print(s)

def global_local_variables():
    print("\n****** Global and Local Variables ******")

    global_local_variables_helper()
    print(s)

def non_local_variables():
    print("\n****** NonLocal Variables ******")
    s = "I love Paris!"
    def nested_func():
        nonlocal s
        s = "I Love Valencia!"
    print("before calling nested_func() s = " + s)
    print("calling nested_func() now:")
    nested_func()
    print("After calling nested_func() s = " + s)

def nested_global_variables():
    print("\n****** Nested Global Variables ******")
    def nested_func():
        global s
        s = "I Love Valencia!"
    print("before calling nested_func() s = " + s)
    print("calling nested_func() now:")
    nested_func()
    print("After calling nested_func() s = " + s)

# Global variables
s = "I love Skopje!"

def main():
    # basics()
    # advanced()
    # global_local_variables()
    # non_local_variables()
    nested_global_variables()
    print("s in main: " + s)


if __name__ == '__main__':
    main()