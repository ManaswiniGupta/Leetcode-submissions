class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d=Counter(nums)
        if len(nums)%2!=0:
            return False
        for i in d.values():
            if i%2!=0:
                return False
        return True
        
