class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r=Counter(ransomNote)
        m=Counter(magazine)
        for i in r.keys():
            if r[i]>m[i]:
                return False
        return True
        
        
