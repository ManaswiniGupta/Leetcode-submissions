class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        s=0
        e=len(nums)-1
        while (s<=e):
            mid=int((s+e)/2)
            if nums[mid]==target:
                return True
            if nums[s]==nums[mid]:
                s+=1
            
                continue
            if nums[s]<=nums[mid]:
                if nums[s]<=target and nums[mid]>=target:
                    e=mid-1
                else:
                    s=mid+1
            else:
                if nums[mid]<=target and target<=nums[e]:
                    s=mid+1
                else:
                    e=mid-1
        return False
        