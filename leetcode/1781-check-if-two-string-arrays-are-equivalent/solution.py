class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s=""
        for i in word1:
            s+=i
        k=""
        for j in word2:
            k+=j
        return s==k

        
