class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        total_pairs=0
        for  count in d.values():
            pairs = (count * (count - 1)) // 2
            total_pairs += pairs
            
        return total_pairs
        
