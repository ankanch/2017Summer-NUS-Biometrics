
# Q3:Read a string from console. Split the string on space delimiter (” ”) and join using a hy-
#    phen (”-”). (Example: input the string ”this is a string” and output as ”this-is-a-string”) (1)
def Q3():
    xstr = input("please input a string: ")
    print("-after split space and join hyphen:","-".join([x for x in xstr.split(" ") if len(x) > 0]))


Q3()