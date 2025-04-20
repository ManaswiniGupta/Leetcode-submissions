class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # m=0
        # for i in range(1,2001):
        #     if i not in arr and k>0:
        #         m=i
        #         k-=1
        # return m
        for i in range(len(arr)):
            if arr[i]<=k:
                k+=1
        return k

        