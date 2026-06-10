class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        total=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                total+=nums[i]
                
            else:
                ans=max(ans, total)
                total=nums[i]
        ans=max(ans,total)
        return ans

        
        
