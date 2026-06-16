class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=""
        i=0
        j=0
        while i<len(word1) and j<len(word2):
            s+=word1[i]+word2[j]
            i+=1
            j+=1
        if word2[j:]:
            s+=word2[j:]
        else:
            s+=word1[i:]
        return s

        
