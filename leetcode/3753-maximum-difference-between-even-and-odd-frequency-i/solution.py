class Solution:
    def maxDifference(self, s: str) -> int:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        
        fa= float('inf')
        fb=0
        for i in d.values():
            if i%2==0:
                fa=min(i,fa)
            else:
                fb=max(i,fb)
        return fb-fa

        
        
