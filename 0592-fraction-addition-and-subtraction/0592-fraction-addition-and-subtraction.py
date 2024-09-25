class Solution:
    def fractionAddition(self, expression: str) -> str:
        import math ,re 
        numbers = list(map(int,re.findall(r"[+-]?\d+", expression)))
        numerator = 0
        denominator = 1

        for i in range(0, len(numbers),2):
           num, den = numbers[i], numbers[i+1]
           numerator = numerator * den +  denominator * num
           denominator *= den

        divisor = math.gcd(numerator, denominator)
        return f"{numerator//divisor}/{denominator//divisor}"