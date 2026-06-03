class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        
        for i in nums:
            d[i]=d.get(i,0)+1
            # Sort the keys by their counts and slice the top K immediately
        return sorted(d, key=d.get, reverse=True)[:k]

