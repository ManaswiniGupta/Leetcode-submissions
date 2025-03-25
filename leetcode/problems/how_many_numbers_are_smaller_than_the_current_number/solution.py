class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        tnums=sorted(nums)
        d={}
        r=[]
        n=len(nums)
        for i in range(len(tnums)):
            if tnums[i] not in d:
                d[tnums[i]]=i
        for i in range(len(nums)):
            r.append(d[nums[i]])
        return r

            
        