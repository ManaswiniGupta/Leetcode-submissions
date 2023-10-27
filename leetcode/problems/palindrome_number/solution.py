class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            l=int(str(x)[::-1])
            if x==l:
                return True
            else:
                return False