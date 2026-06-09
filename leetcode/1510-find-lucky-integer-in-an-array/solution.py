class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d={}
        for i in arr:
            d[i]=d.get(i,0)+1
        maxi=-1
        for i in d.keys():
            if d[i] == i:
                maxi=max(maxi, i)
        return maxi
        
