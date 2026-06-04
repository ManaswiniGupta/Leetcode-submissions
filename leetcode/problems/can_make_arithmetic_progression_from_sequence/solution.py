class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr=sorted(arr)
        k=abs(arr[0]-arr[1])
        for i in range(len(arr)-1):
            if k==arr[i+1]-arr[i]:
                pass
            else:
                return False
        return True



        