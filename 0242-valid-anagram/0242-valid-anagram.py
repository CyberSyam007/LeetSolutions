class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        k="".join(sorted(s))
        l="".join(sorted(t))
        if k==l:
            return True
        else:
            return False
        