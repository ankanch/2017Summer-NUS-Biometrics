def gcd(a,b):
    while b>0:
        r = a%b
        a,b=b,r
    return a

def factorial(x):
    z = 1
    for t in range(1,x+1):
        z *=t
    return z
    """
    if x == 1:
        reutrn 1
    return x*factorial(x-1)
    """

def xx(x):
    if len(x) < 2:
        return ""
    return x[:2]+x[len(x)-2:len(x)]
    # x[:2]+x[-2:]

def P(x):
    for x,y in zip(x,x[::-1]):
        if x != y:
            return False
    return True

print(P("1233"))
print(P("121"))
print(P(""))