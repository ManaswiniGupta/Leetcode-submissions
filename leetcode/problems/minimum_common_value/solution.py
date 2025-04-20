class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        for i in nums1:
            s=0
            e=len(nums2)-1
            while s<=e:
                mid=int((s+e)/2)
                if nums2[mid]==i:
                    return i
                elif nums2[mid]>i:
                    e=mid-1
                else:
                    s=mid+1
        return -1

        