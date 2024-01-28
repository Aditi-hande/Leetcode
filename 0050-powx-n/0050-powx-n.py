class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1

        result, base = 1, x

        if n < 0:
            n = -n
            base = 1 / x

        while n > 0:
            if n % 2 == 1:
                result *= base
            base *= base
            n //= 2

        return result
