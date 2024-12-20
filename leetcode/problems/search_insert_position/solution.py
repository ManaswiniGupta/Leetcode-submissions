class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s=0
        e=len(nums)-1
        while s<=e:
                m=int((s+e)/2)
                if target==nums[m]:
                    return m
                elif nums[m]<target:
                    s=m+1
                else:
                    e=m-1
        return s
            


        