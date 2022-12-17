from math import sqrt

class SecondDegree:
    def __init__(self) -> None:
        self.polynomial = input("Insert a second-degre polynomial (ax**2+bx+c): ")
        self.a, self.b, self.c = self.set_parameters()
        self.
    def set_parameters(self):
        copy = self.polynomial
        prov_a=[]
        prov_b=[]
        if "x**2" in copy:
            for n in copy:  #set prov_a
                if n != "x":
                    prov_a.append(n)
                    copy = copy.replace(n, "")
                else:
                    copy = copy.replace("x**2", "")
                    break
        if "x" in copy: #Set prov_b
            for n in copy:
                if n !="x":
                    if n != "+":
                        prov_b.append(n)
                        copy = copy.replace(n, "")
                else:
                    copy = copy.replace("x", "")
                    break
        copy = copy.replace("+", "")    #set prov_c

        # Now I can get the real values
        a = int("".join(prov_a))
        b = int("".join(prov_b))
        c = int("".join(copy))

        return a,b,c
    def get_roots(self):
        if (self.b**2 - 4*self.a*self.c) < 0:
            print("There are no real roots in this polynomial.")
            return 
        else:
            

    
pol = SecondDegree()