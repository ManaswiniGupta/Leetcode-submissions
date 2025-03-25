class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        s=1
        e=x//2
        while s<=e:
            mid=(s+e)//2
            sq=mid*mid
            if x==sq:
                return mid
            elif x>sq:
                s=mid+1
            else:
                e=mid-1
        return e

