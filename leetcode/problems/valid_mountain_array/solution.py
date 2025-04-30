class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        m=arr.index(max(arr))
        
        if len(arr)<3 or m==0 or m==len(arr)-1:
            return False
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                return False
            if i<m and (arr[i]<arr[i+1]):
                continue
            elif i == m:
                continue  
            elif i>m and (arr[i]>arr[i+1]):
                continue
            else:
                return False
        return True

        
            





            
    
        