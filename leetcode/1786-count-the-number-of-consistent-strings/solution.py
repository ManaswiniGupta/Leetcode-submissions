class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        allowd=set(allowed)
        for i in words:
            if set(i) <= allowd:
                count+=1
        return count
