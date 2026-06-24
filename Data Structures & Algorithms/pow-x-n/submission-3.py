class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def find_power(x, n):
            if n == 0:
                return 1

            elif n == 1:
                return x
            
            elif n < 0:
                x = 1/x
                n = -n
                return x * find_power(x, n-1)
            
            else:
                return x * find_power(x, n-1)
        
        return find_power(x, n)
