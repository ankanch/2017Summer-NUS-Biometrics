# Q2:Read a string from console and output its length, swap its cases, convert it to lower
#    case and upper case, and reverse it. (Hint: try string slice with step -1) (3)
def Q2():
    xstr = input("please input a string: ")
    print("-length of the string is",len(xstr))
    print("-after swaping cases:",xstr.swapcase())
    print("-convert to UPPER case:",xstr.upper())
    print("-convert to lower case:",xstr.lower())
    print("-reverse string:",xstr[::-1])

Q2()