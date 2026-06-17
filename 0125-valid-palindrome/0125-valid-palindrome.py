import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=re.sub(r'[^a-z0-9]','',s)
        s1=s[::-1]
        if s==s1:
            return True
        else:
            return False

        