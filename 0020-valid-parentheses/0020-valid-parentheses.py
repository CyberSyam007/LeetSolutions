class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        counter=-1
        openB=['(','{','[']
        for i in s:
            if i  in openB:
                stack.append(i)
                counter+=1
            elif i == '}' :
                if  counter > -1 and  stack[counter]=='{' :
                    stack.pop()
                    counter-=1
                else:
                    return False
            elif i == ')':
                if counter > -1 and  stack[counter]=='('  :
                    stack.pop()
                    counter-=1
                else:
                    return False
            elif i == ']':
                if counter > -1 and stack[counter] == '[' :
                    stack.pop()
                    counter-=1
                else:
                    return False
        if len(stack)!=0:
            return False
        else:
            return True

                 
        