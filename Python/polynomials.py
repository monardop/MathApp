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
        copy = copy.replace(" ", "")
        prov_a=[]
        prov_b=[]
        try:
            if "x**2" in copy:
                for n in copy:  #set prov_a
                    if n != "x":
                        prov_a.append(n)
                        copy = copy.replace(n, "",1)
                    else:
                        copy = copy.replace("x**2", "")
                        break
            else:
                prov_a = 0
                len(prov_a)
        except TypeError:
            print("This is not a quadratic function")
            exit(1)
        else:
            if "x" in copy: #Set prov_b
                for n in copy:
                    if n !="x":
                        if n != "+":
                            prov_b.append(n)
                            copy = copy.replace(n, "",1)
                    else:
                        copy = copy.replace("x", "")
                        break
            else:
                prov_b = "0"
            copy = copy.replace("+", "")    #set prov_c

            # Now I can get the real values
            values = []
            for n in [prov_a, prov_b]:
                if len(n) !=0:
                    values.append(int("".join(n)))
                else:
                    values.append(1)

            if len(copy) != 0:
                values.append(int("".join(copy)))
            else:
                values.append(0)

            return values
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
        plt.plot(self.vertex[0], self.vertex[1], "o")
        if self.a > 0:
            plt.annotate(str(self.vertex),xy=(self.vertex[0]-2, self.vertex[1]-10))
        else:
            plt.annotate(str(self.vertex),xy=(self.vertex[0]-2, self.vertex[1]+10))

        if self.roots != None:
            ax = plt.gca()
            ax.spines['bottom'].set_position(('data',0))
            plt.plot(self.roots[0], 0, "o")
            plt.plot(self.roots[1], 0, "o")    
        plt.grid()
        plt.show()
    def show_info(self) -> None:
        print(f"Your quadratic function: {self.a}x^2 + {self.b}x + {self.c}")
        print(f"Its vertex: {self.vertex}")
        print(f"Its roots: {self.roots}")
        print(f"y-axis intersection: (0,{self.c})")
        self.show_graph()