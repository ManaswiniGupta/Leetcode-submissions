class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        for nums in nums1:
            if nums in nums2 and nums not in l:
                l.append(nums)
        
        return l
        