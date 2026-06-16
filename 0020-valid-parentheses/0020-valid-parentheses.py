class Solution:
    def isValid(self, s: str) -> bool:
        d={'}' : '{', ')':'(' , ']':'['}
        stack=[]
        for i in s:
            if i in d.values():
                stack.append(i)
            elif i in d:
                if len(stack)==0:
                    return False
                x= stack.pop()
                if x != d[i]:
                    return False
        if len(stack) !=0:
            return False
        else:
            return True



        