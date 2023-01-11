class Fraction:
    def __init__(self, dividend: int, divisor=1) -> None:
        self.dividend = dividend
        self.divisor = divisor
        self.nominator, self.denominator = self.get_fraction()

    def get_fraction(self) -> tuple:
        """
        This function get the simplified version of the division that the user put as an input
        :return:
        A fraction simplified
        """
        nominator = self.dividend
        denominator = self.divisor

        if nominator/denominator == int(nominator/denominator):
            return int(nominator/denominator), 1

        while True:
            if nominator % 10 == 0 and denominator % 10 == 0:
                nominator /= 10
                denominator /= 10
            elif nominator % 5 == 0 and denominator % 5 == 0:
                nominator /= 5
                denominator /= 5
            elif nominator % 3 == 0 and denominator % 3 == 0:
                nominator /= 3
                denominator /= 3
            elif nominator % 2 == 0 and denominator % 2 == 0:
                nominator /= 2
                denominator /= 2
            else:
                break

        return int(nominator), int(denominator)

    def get_mix_fraction(self) -> str:
        if self.nominator < self.denominator:
            return self
        int_part: int = self.nominator // self.denominator
        b = Fraction(int_part * self.denominator, self.denominator)
        return f"{int_part} {self - b}"

    def __add__(self, fraction):
        try:
            new_nominator = (self.nominator * fraction.denominator
                                 + fraction.nominator * self.denominator)
            new_denominator = self.denominator * fraction.denominator
        except AttributeError:
            a = Fraction(fraction, 1)
            new_nominator = (self.nominator * a.denominator
                             + a.nominator * self.denominator)
            new_denominator = self.denominator * a.denominator

        return Fraction(new_nominator, new_denominator)

    def __sub__(self, fraction):
        try:
            new_nominator = (self.nominator * fraction.denominator
                             - fraction.nominator * self.denominator)
            new_denominator = self.denominator * fraction.denominator
        except AttributeError:
            a = Fraction(fraction, 1)
            new_nominator = (self.nominator * a.denominator
                             - a.nominator * self.denominator)
            new_denominator = self.denominator * a.denominator

        return Fraction(new_nominator, new_denominator)

    def __mul__(self, fraction):
        try:
            new_nominator = self.nominator * fraction.nominator
            new_denominator = self.denominator * fraction.denominator
        except AttributeError:
            new_nominator = self.nominator * fraction
            new_denominator = self.denominator

        return Fraction(new_nominator, new_denominator)

    def __truediv__(self, other):
        try:
            new_nominator = self.nominator * other.denominator
            new_denominator = self.denominator * other.denominator
        except AttributeError:
            new_nominator = self.nominator
            new_denominator = self.denominator * other

        return Fraction(new_nominator, new_denominator)

    def __pow__(self, power):
        return Fraction(self.nominator ** power, self.denominator ** power)

    def __str__(self) -> str:
        if self.denominator != 1:
            return f"{self.nominator}/{self.denominator}"
        else:
            return f"{self.nominator}"

    def get_decimal(self) -> float:
        return self.nominator / self.denominator


def create_fraction(number: float) -> Fraction:
    """
    This function returns a fraction from a float number.
    """
    # First: I get the number of decimals
    aux = str(number)
    integer, decimal = aux.split(".")

    # Now I set the denominator
    denominator = 10 ** len(decimal)
    nominator = number * denominator

    return Fraction(nominator, denominator)
