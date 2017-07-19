#encoding:utf-8
# by Long Zhang @ Jul 17
# kanchisme@gmail.com


# Q1 : Add numbers from 100 to 200
def Q1():
    # while loop version
    x = 100
    xsum = 0
    while x <= 200:
        xsum += x
        x+=1
    print("-using while loop:",xsum)

    # for loop version
    xsum = 0
    for x in range(100,201):
        xsum += x
    print("-using for loop:",xsum)


# Q2:Read a string from console and output its length, swap its cases, convert it to lower
#    case and upper case, and reverse it. (Hint: try string slice with step -1) (3)
def Q2():
    xstr = input("please input a string: ")
    print("-length of the string is",len(xstr))
    print("-after swaping cases:",xstr.swapcase())
    print("-convert to UPPER case:",xstr.upper())
    print("-convert to lower case:",xstr.lower())
    print("-reverse string:",xstr[::-1])


# Q3:Read a string from console. Split the string on space delimiter (” ”) and join using a hy-
#    phen (”-”). (Example: input the string ”this is a string” and output as ”this-is-a-string”) (1)
def Q3():
    xstr = input("please input a string: ")
    print("-after split space and join hyphen:","-".join([x for x in xstr.split(" ") if len(x) > 0]))


# Q4:Learn the Python list operations and follow the commands
def Q4():
    L = []
    print("-initialize the list:",L)
    L.extend([12,8,9])
    print("-after add 12 8 9 to the list:",L)
    L.insert(0,9)
    print("-insert 9 to the head of the list:",L)
    L*=2
    print("-double the list:",L)
    L = [x for x in L if x != 8]
    print("-remove all 8 in L",L)
    L=L[::-1]
    print("-reverse the list:",L)


# Q5:. A cryptarithmetic puzzle
def Q5():
    def isPZCZ(n):
        """Predicate to check that n, the input number,
        has the format PZCZ, i.e. the 2nd and 4th digits are equal.
        n: input number, assumed to be 4 digits
        Returns True if n has the format PZCZ, False otherwise."""
        # convert to str
        x = str(n)

        # then we check
        if x[1] == x[3]:
            return True
        return False
    def isProductMUCHZ(pzcz, product):
        """Predicate to check that product has the format MUCHZ.
        pzcz: input number, assumed to be in format PZCZ
        product: input number
        More precisely, this predicate checks 3 things:
        (i) that product has exactly 5 digits
        (ii) that the last digit of product is Z, the last digit of pzcz
        (iii) that the 3rd digit of product is C, the 3rd digit of pzcz.
        Returns True if product passes all 3 checks, False otherwise."""
        # convert to str
        p = str(product)
        n = str(pzcz)

        # then we check
        if len(p) == 5:
            if p[-1] == n[-1] and p[2] == n[2]:
                return True
        return False 
    S = [(x,x*15) for x in range(1000,10000) if isPZCZ(x) and isProductMUCHZ(x,x*15)]
    print("-All solutions to the cryptarithmetic puzzle are:\n",S)
 

# used for testing
if __name__ == "__main__":
    Quizs = [Q1,Q2,Q3,Q4,Q5]
    for index,quiz in enumerate(Quizs):
        print("\n>>>>>>>>>>>>>>>>>>>>>>>Result of quiz %d" % (index+1),"as below<<<<<<<<<<<<<<<<<<<<<<\n")
        quiz()