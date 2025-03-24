class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # for i in range(0,len(nums)+1):
        #     if i in nums:
        #         continue
        #     else:
        #         return i
        nums.sort()
        i=0
        if nums[0]!=0:
            return 0
        elif nums[-1]!=len(nums):
            return len(nums)
        else:
            for j in range(0,len(nums)):
                if j!=nums[j]:
                    return j
                else:
                    continue
            

        