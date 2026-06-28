class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def find_power(x, n):
            if n <= 1:
                return x
            else:
                return x * find_power(x, n-1)
        
        return find_power(x, n)
