class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        z=0
        for i in nums:
            z^=i
        return z
        