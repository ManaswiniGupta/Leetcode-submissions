class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        s=sorted(heights)
        ans=0
        for i in range(len(s)):
            if s[i]!=heights[i]:
                ans+=1
        return ans
        
        
