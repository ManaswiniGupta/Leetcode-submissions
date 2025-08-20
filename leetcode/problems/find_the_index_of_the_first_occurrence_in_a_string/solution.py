class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else:
            a=0
            for i in haystack:
                if i==needle[0] and haystack[a:a+len(needle)]==needle:
                    return a
                a+=1
            
            

        