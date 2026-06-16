class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        # for i in range(len(nums)):
        #     nums[i]=nums[i]**2
        # nums.sort()
        # return nums
        l=0
        r=len(nums)-1
        k= len(nums)-1
        res=[0]*len(nums)
        while l<r:
            if nums[l]**2<nums[r]**2:
                res[k]=nums[r]**2
                r-=1  
            else:
                res[k]=nums[l]**2
                l+=1
            k-=1
        if r==l:
            res[0]=nums[r]**2
        return res



        
