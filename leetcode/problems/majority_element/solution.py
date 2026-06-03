class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count=0
        # candidate=0
        # for nums in nums:
        #     if count==0:
        #         candidate=nums
        #     if nums==candidate:
        #         count+=1
        #     else:
        #         count-=1
        # return candidate
        threshold=len(nums)//2
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
            if d[i]>threshold:
                return i

        
        

        