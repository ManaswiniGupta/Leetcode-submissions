class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        incr=1
        decr=1
        ans=1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                incr+=1
            else:
                incr = 1
        
            if nums[i]>nums[i+1]:
                decr+=1
            else:
                decr = 1
            ans=max(incr, decr, ans)
        return ans

        
