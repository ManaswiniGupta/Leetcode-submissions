class Solution:
    def average(self, salary: List[int]) -> float:
        mini=salary[0]
        maxi=0
        sum=0
        for i in range(len(salary)):
            sum+=salary[i]
            if salary[i]>maxi:
                maxi=salary[i]
            if salary[i]<mini:
                mini=salary[i]
        sum=sum-maxi-mini
        return sum/(len(salary)-2)

        