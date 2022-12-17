from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

class SecondDegree:
    def __init__(self) -> None:
        self.polynomial = input("Insert a second-degre polynomial (ax**2+bx+c): ")
        self.a, self.b, self.c = self.set_parameters()
        self.vertex = self.get_vertex()
        self.roots = self.get_roots()
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
    def get_vertex(self) -> tuple:
        x_vortex = (-1*self.b) / (2*self.a)
        y_vortex = self.a*(x_vortex**2) + self.b*(x_vortex) + self.c
        return (x_vortex, y_vortex)
    def get_roots(self):
        square_root = (self.b**2) - (4*self.a*self.c)
        if square_root < 0:
            print("There are no real roots in this polynomial.")
            return 
        else:
            x_1= self.vertex[0] + (sqrt(square_root) / (2*self.a))
            x_2= self.vertex[0] - (sqrt(square_root) / (2*self.a))
            return (x_1, x_2)
    def show_graph(self):
        x = np.linspace(-10, 10, 30)
        y = self.a*(x**2) + self.b*x + self.c
        plt.plot(x,y)
        plt.plot(self.vertex[0], self.vertex[1])
        plt.show()
    def show_info(self) -> None:
        print(f"Your quadratic function: {self.polynomial}")
        print(f"Its vertex: {self.vertex}")
        print(f"Its roots: {self.roots}")
        self.show_graph()

pol = SecondDegree().show_info()