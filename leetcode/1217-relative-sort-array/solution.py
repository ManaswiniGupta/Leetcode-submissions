class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d={}
        for i in arr1:
            d[i]=d.get(i,0)+1
        l=[]
        for i in range(len(arr2)):
            l+=[arr2[i]]*d[arr2[i]]
        s=[]
        for i in arr1:
            if i not in l:
                s.append(i)
        l=l+sorted(s)
        return l
        
