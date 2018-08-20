def essentials():
    print("\n****** String Essentials ******")

    s1 = "I'm going to Valencia"                                                                                                            # if you want to use the character ' in your string, use " (double quotes) to define the string
    print(s1)

    s2 = "Vasil\nBuraliev"                                                                                                                  # \n stands for new line (linefeed)
    print(s2)

    s3 = "Vasil\tBuraliev"                                                                                                                  # \n stands for tab
    print(s3)

    s4 = "Vasil\vBuraliev"                                                                                                                  # \v stands for vertical tab
    print(s4)

    s5 = "Vasil\fBuraliev"                                                                                                                  # \v stands for Formfeed
    print(s5)

    print("The string '%s' has %s characters, including white spaces" % (s1, len(s1)))                                                      # the len() founction counts character of the string variable

def advanced():
    print("\n****** Advanced operations with string variables ******")

    s1 = 'Васил Буралиев'                                                                                                                   # unicode is supported
    print("Unicode characters are supported '%s'" % (s1))

    print('If you want to use the characters such as \' then, you will have to use backslash in front of them such as \\\' ')               # writing special characters is sibgle quoted defined strings. The same stands for double quotes.

    s2 = s1
    print ("the variables s1(%s) and s2(%s) are referencing to the same memory location: %s" % (s1, s2, s1 is s2))                          # not always correct/true statement 's1 == s2' means 's1 is s2' is true

    s3 = b"Vasil Buraliev"
    print("'s3' variable is of type: %s" % type(s3))
    t = str(s3)
    print("'t' variable is of type: %s" % type(t))
    u = t.encode("UTF-8")
    print("'u' variable is of type: %s" % type(u))



def indexing_and_slicing():
    print("\n****** String indexing and Slicing ******")

    s1 = "My name is Vasil"
    print("Take fist character of the string '%s' which is %s" % (s1, s1[0]))                                                                   # Take the first character of a string (indexing starts from 0)
    print("Negative indexing. Take last character of the string '%s' which is %s" % (s1, s1[-1]))                                               # take the last character of a string (negative indexing)
    print("Take substring from a string. (slicing). Take substring from the middle of the string '%s' which is '%s'" % (s1, s1[3:7]))           # [start index : end index(not included)]
    print("Another representation (s1[::]) of a string '%s'" % (s1[::]))                                                                        # [start index : end index(not included) : step]
    print("Get every second character fromt he string '%s' which is '%s'" % (s1, s1[::2]))                                                      # use steps in slicing a string
    print("Get me reverse string of '%s' by a Python style which '%s'" % (s1, s1[::-1]))                                                        # Python style reverse string by slicing syntax

def properties_and_methods():
    print("\n****** String Properties and Methods ******")

    s1 = "Vasil Buraliev"
    try:
        s1[0] = 'P'                                                                                                                             # strings ar immutable. New variable has to be created
    except Exception as e:
        print("[Error] ", e)

    s2 = "is from Skopje"
    print("Contatenation of two strings, '%s' and '%s' and the result is '%s'" % (s1, s2, s1 + " " + s2))                                       # + operator can be used for string concatenation

    s3 = 'z'
    i = 10
    print ("I can multiply string '%s' with a number '%s' and the result is '%s'. " % (s3, i, s3 * i))                                          # string can be multiplied easily by using multiplication operator

    try:
        print ("Try to contatenate string '%s' and integer '%s'." % (s3, i))
        s3 + i                                                                                                                                  # it's not posible to concatinate string and integer (different types of variables)
    except Exception as e:
        print("[Error] ", e)


    s4 = "Playing with Python string methods"
    print("Upper method applied on string '%s' resulted with '%s'" % (s4, s4.upper()))                                                          # string has many functions that can be applied on a string. 'upper' is one of them
    print("Split the string '%s' in a tupple resulted with %s" % (s4, s4.split(" ")))                                                           # splitting a string by specific character. In this case white space, which is default delimiter.


def formating():
    print("\n****** String Formating ******")

    print("This is a string {}".format("INSERTED"))                                                                                             # plancehoder {} can be replaced with value of a variable
    print("The {2} {1} {0}".format("fox", "orange", "quick"))                                                                                   # a placeholder {0 based index number} can include a number
    print("The {q} {o} {f}".format(f="fox", o="orange", q="quick"))                                                                             # define variables and use it in a placeholder {variable}
    print("The {q} {q} {q}".format(f="fox", o="orange", q="quick"))

    print("The {0:<40s}".format("Left aligned"))                                                                                                # left aligned
    print("The {0:>40s}".format("Right aligned"))                                                                                               # right aligned

    long_result = 2142352346
    print("Thousands with commas {0:,}".format(long_result))                                                                                    # insert the character , (comma) for thousands

    s1 = "Vasil Buraliev"
    print(f"Hello, my name is {s1}")                                                                                                            # Python 3.6 new style formating of a string

    result = 123.5678940
    print("Return some floating point value {r}".format(r=result))
    print("Return some formated floating point value {r:10.2f}".format(r=result))                                                               # format floating point example
    print("Return another formated floating point value {r:1.2E}".format(r=result))

    i_result = 123
    print("Return octal format %10.3o" % (i_result))
    print("Return hecadecimal format %10.3x" % (i_result))
    print("Return zero formated hecadecimal value %010x" % (i_result))                                                                          # zero padded value
    print("Return hecadecimal format, left alignment %-10x" % (i_result))                                                                       # left alignment



def main():
    print("\n****** Main Function Workings with Strings ******")

    # essentials()
    # advanced()
    # indexing_and_slicing()
    # properties_and_methods()
    formating()


if __name__ == '__main__':
    main()