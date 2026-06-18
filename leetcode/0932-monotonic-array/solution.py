class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        arr_is =""
        if nums[0]<=nums[len(nums)-1]:
            arr_is+="inc"
        else:
            arr_is+="dec"
        i=0
        for j in range(1,len(nums)):
            if i <= j and nums[i] <= nums[j] and arr_is=="inc":
                i+=1
            elif i <= j and nums[i] >= nums[j] and arr_is=="dec":
                i+=1
            else:
                return False
        return True 

        # nums2=sorted(nums)
        # if nums==nums2 or nums==nums2[::-1]:
        #     return True
        # return False

        
