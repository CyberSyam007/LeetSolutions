class Solution:
    def countBits(self, n: int) -> List[int]:

        def ones(x):
            counter=0
            while x>0:
                if x>0 and x&1!=0:
                    counter+=1
                x>>=1
            return counter

        x=n+1
        l=[]
        for i in range(x):
            l.append(ones(i))
        return l

    