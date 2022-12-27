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

    def __add__(self, fraction):
        if fraction is int:
            new_nominator = self.nominator + fraction * self.denominator
            new_denominator = self.denominator
        else:
            new_nominator = (self.nominator * fraction.denominator
                             + fraction.nominator * self.denominator)
            new_denominator = self.denominator * fraction.denominator

        return Fraction(new_nominator, new_denominator)

    def __sub__(self, fraction):
        new_nominator = (self.nominator * fraction.denominator
                         - fraction.nominator * self.denominator)
        new_denominator = self.denominator * fraction.denominator

        return Fraction(new_nominator, new_denominator)

    def __mul__(self, fraction):
        new_nominator = self.nominator * fraction.nominator
        new_denominator = self.denominator * fraction.denominator

        return Fraction(new_nominator, new_denominator)

    def __pow__(self, power: int):
        return Fraction(self.nominator ** power, self.denominator ** power)

    def __str__(self) -> str:
        if self.denominator != 1:
            return f"{self.nominator}/{self.denominator}"
        else:
            return f"{self.nominator}"


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


def sqrt(fraction: Fraction) -> float:
    new_nom = fraction.nominator ** (1 / 2)
    new_den = fraction.denominator ** (1 / 2)
    return new_nom / new_den


def cube_root(fraction: Fraction) -> float:
    new_nom = fraction.nominator ** (1 / 3)
    new_den = fraction.denominator ** (1 / 3)
    return new_nom / new_den


def get_decimal(fraction: Fraction) -> float:
    return fraction.nominator / fraction.denominator


def get_mix_fraction(fraction: Fraction) -> str:
    pass
    # TODO: mixed fractions
    # TODO: create a function that add/sub ints to fractions
