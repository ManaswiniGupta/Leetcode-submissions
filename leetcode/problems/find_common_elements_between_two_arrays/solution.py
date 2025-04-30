class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        co=0
        c=0
        for i in nums1:
            if i in nums2:
                co+=1
        for i in nums2:
            if i in nums1:
                c+=1
        return [co,c]

        