class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        #         else:
        #             continue
        
        diction={}
        n=len(nums)
        for i in range(n):
            diction[nums[i]]=i
        for i in range(n):
            complement=target-nums[i]
            if complement in diction and diction[complement] != i:
                return [i, diction[complement]]
        return [] 
