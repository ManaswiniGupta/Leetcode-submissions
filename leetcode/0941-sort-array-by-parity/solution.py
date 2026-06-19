class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i=0
        j=len(nums)-1
        while i<j:
            if nums[i]%2!=0 and nums[j]%2==0: #oe
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
            elif nums[i]%2!=0 and nums[j]%2!=0: #oo
                j-=1
            elif nums[i]%2==0 and nums[j]%2==0: #ee
                i+=1
            else: #eo
                i+=1
                j-=1
        return nums

        
