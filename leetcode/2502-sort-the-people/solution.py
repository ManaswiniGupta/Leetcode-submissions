class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pairs = list(zip(heights, names))
        
        # 2. Sort by height (which is index 1 of the pair) in descending order
        pairs.sort(reverse=True)
        return [name for _, name in pairs]
        
