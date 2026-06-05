class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        left=0
        right=0
        ans=1
        curr= s[left:right+1]
        while right<len(s)-1:
            if s[right+1] not in curr:
                right+=1
                curr=s[left:right+1]
                ans=max(ans, len(curr))
            elif s[right+1] in curr:
                left+=1
                curr=s[left:right+1]
                
        return ans
            
            

            