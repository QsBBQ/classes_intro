import fractions

# in case I need to numb my brain
# http://www.ics.uci.edu/~eppstein/numth/frap.c
# fractions.Fraction(".20") == fractions.Fraction("1/5")

class Fraction:
    def __init__(self, numerator, denominator):
        # Best way to allow float and numerator, denominator?
        self.gcd = fractions.gcd(numerator, denominator)
        self.num = numerator/self.gcd
        self.den = denominator/self.gcd

    def __repr__(self):
        vulgar = divmod(self.num, self.den)
        if vulgar[0] == 0:
            return '%s/%s' % (self.num, self.den)
        else:
            self.num_vulgar = vulgar[1]
            return '%s %s/%s' % (vulgar[0], self.num_vulgar, self.den)

    def __add__(self, other):
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __sub__(self, other):
        num = self.num * other.den - self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den)

    def __div__(self, other):
        return Fraction(self.num * other.den, self.den * other.num)

    def __eq__(self, other):
        return (self.num/float(self.den) == other.num/float(other.den))

    def __ne__(self, other):
        # return(self.num/float(self.den) != other.num/float(other.den))
        return not self.__eq__(other)

    def __lt__(self, other):
        # print("lt")
        return(self.num/float(self.den) < other.num/float(other.den))

    def __gt__(self, other):
        # print("gt")
        return(self.num/float(self.den) > other.num/float(other.den))

f1 = Fraction(9, 4)
# print("from __repr__")
print(f1)
f2 = Fraction(1, 4)
# print(f2)
f_plus = f1+f2
print(f_plus)
# f_minus = f1-f2
# print(f_minus)
# f_equal = f1 == f2
# print(f_equal)
# f_nequal = f1 != f2
# print(f_nequal)
# f_lt = f1 < f2
# print(f_lt)
# f_gt = f1 > f2
# print(f_gt)
