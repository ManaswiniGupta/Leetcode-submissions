class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s, e = 0, len(nums) - 1
        mi = -1
        while s <= e:
            m = (s + e) // 2
            if nums[m] < target:
                s = m + 1
            else:
                if nums[m] == target and (m == 0 or nums[m - 1] < target):
                    mi = m
                e = m - 1
        
        s, e = 0, len(nums) - 1
        mx = -1
        while s <= e:
            m = (s + e) // 2
            if nums[m] <= target:
                if nums[m] == target and (m == len(nums) - 1 or nums[m + 1] > target):
                    mx = m
                s = m + 1
            else:
                e = m - 1
        
        return [mi, mx]
