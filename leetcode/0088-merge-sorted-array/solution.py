class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:]=nums1[:m]
        i=0
        j=0
        while i<len(nums1) and j<n:
            if nums1[i]<=nums2[j]:
                i+=1
            else:
                nums1.insert(i,nums2[j])
                i+=1
                j+=1
        while j < n:
            nums1.append(nums2[j])
            j += 1
       
        
