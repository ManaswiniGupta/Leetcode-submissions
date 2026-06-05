class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr=sum(arr[:k])/k
        count=0
        # first window check
        if curr>=threshold:
                count+=1
        for i in range(k, len(arr)):
            curr+=(arr[i]-arr[i-k])/k
            if curr>=threshold:
                count+=1
        return count
        