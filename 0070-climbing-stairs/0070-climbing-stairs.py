import math
class Solution:
    

    
    def climbStairs(self, n: int) -> int:
        def calways(n1,n2):
            temp=(math.factorial(n1+n2))//(math.factorial(n1)* math.factorial(n2))
            return temp

        c2=0
        c1=n
        n_ways=0
        for c2 in range((n//2)+1):
            c1=n-(2*c2)
            n_ways+=calways(c1,c2)
        return n_ways

            
        
            


         
        
        