class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        sum=0
        for i in range(len(points)-1):
            for j in range(2):
                x=points[i][0]-points[i+1][0]
                y=points[i][1]-points[i+1][1]
            z=max(abs(x),abs(y))
            sum+=z
        
        return sum
        