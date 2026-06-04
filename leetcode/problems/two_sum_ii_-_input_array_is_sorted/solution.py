class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        k=target
        
        while left<right:
                if numbers[left]+numbers[right]>k:
                    right-=1
                elif numbers[left]+numbers[right]==k:
                    return [left+1,right+1]
                else:
                    left+=1
                   
        