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


Q5()