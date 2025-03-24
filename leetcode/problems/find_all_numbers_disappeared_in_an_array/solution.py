class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l=[]
        num_set=set(nums)
        for i in range(1,len(nums)+1):
            if i in num_set:
                continue
            else:
                l.append(i)
        return l

        