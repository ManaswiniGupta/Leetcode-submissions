class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        fs={}
        ft={}
        for i in s:
            fs[i]=fs.get(i,0)+1
        for i in t:
            ft[i]=ft.get(i,0)+1
        return fs==ft


        