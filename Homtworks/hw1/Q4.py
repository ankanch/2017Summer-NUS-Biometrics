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


Q4()