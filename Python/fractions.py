class Fraction:
    def __init__(self, dividend, divisor) -> None:
        self.dividend = dividend
        self.divisor = divisor
        self.nominator, self.denominator = self.get_fract()
        
    def get_fract(self)->tuple:
        nominator = self.dividend
        denominator = self.divisor

        while True:
            if nominator%10 == 0 and denominator%10 ==0:
                nominator /= 10
                denominator /=10
            elif nominator%5 == 0 and denominator%5 ==0:
                nominator /= 5
                denominator /=5
            elif nominator%3 == 0 and denominator%3 ==0:
                nominator /= 3
                denominator /=3
            elif nominator%2 == 0 and denominator%2 ==0:
                nominator /= 2
                denominator /=2
            else:
                break
        
        return nominator, denominator

    def __str__(self) -> str:
        return f"{self.nominator}/{self.denominator}"