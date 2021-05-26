
#Kristen Tse
#Data Structures
#6/7/19
#Lab 2


#The Polynomial Class
class Polynomial:
    def __init__(self, lst_coeff = [0]):
        self.lst_coeff = lst_coeff
         
    def __repr__(self):
        ordered_lst = []
        for i in range(len(self.lst_coeff)):
            if self.lst_coeff[i] != 0:
                if i == 0:
                    val = str(self.lst_coeff[i])
                elif i == 1:
                    val = str(self.lst_coeff[i]) + "x"
                else:
                    val = str(self.lst_coeff[i]) + "x^" + str(i)
                ordered_lst.insert(0,val)
        ordered_lst = ("+").join(ordered_lst)
        return (str(ordered_lst))

    def eval(self, num):
        final = 0
        for i in range(len(self.lst_coeff)):
            final += (self.lst_coeff[i] * (num**i)) 
        return final

    def __add__(self, other):
        add_lst = [0] * (max(len(self.lst_coeff), len(other.lst_coeff)))
        for i in range(len(self.lst_coeff)):
            add_lst[i] += self.lst_coeff[i]
        for j in range(len(other.lst_coeff)):
            add_lst[j] += other.lst_coeff[j]
        return Polynomial(add_lst)

    def __mul__(self, other):
        mult_lst = [0] * ((len(other.lst_coeff) * len(self.lst_coeff)))
        for i in range(len(other.lst_coeff)):
            for j in range(len(self.lst_coeff)):
                coeff = other.lst_coeff[i] * self.lst_coeff[j]
                ind = i + j
                mult_lst[ind] += coeff
        return Polynomial(mult_lst)

    def polySequence(self, start, end, step = 1):
        for i in range(0, 5, step):
            final = 0
            for j in range(len(self.lst_coeff)):
                final += (self.lst_coeff[j] * (i**j))
            yield(final)

    def derivative(self):
        deriv_lst = [(self.lst_coeff[i] * i) for i in range(len(self.lst_coeff))]
        return Polynomial(deriv_lst[1:])
        

def main():
    #shows repr and eval
    a = Polynomial([42,-17,0,5])
    b = Polynomial([3, 5, 7, 5])
    print(a)
    print(a.eval(1))

    #shows addition
    c = Polynomial([7, 5, -10, 0, 3])
    d = Polynomial([-2, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2])
    print(c+d)

    #shows multiplication
    e = Polynomial([0, 2, 0, 3])
    f = Polynomial([0, 1, 0, 5, 0, 0, 0, 0, 0, 0, 0, 2])
    print(e*f)

    #shows polySequence kv
    p = Polynomial([1,2])
    for val in p.polySequence(0,5):
        print(val)


    #shows derivative
    x = Polynomial([1, 4, 0, 2])
    print(x.derivative())

main()