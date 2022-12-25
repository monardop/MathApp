class Fraction:
    def __init__(self, dividend, divisor) -> None:
        self.dividend = dividend
        self.divisor = divisor

    def get_fract(self):
        nominator = self.dividend
        denominator = self.divisor
        

    def __str__(self) -> str:
        return f"{self.nominator}/{self.denominator}"