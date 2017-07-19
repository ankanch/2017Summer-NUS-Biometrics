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

Q1()