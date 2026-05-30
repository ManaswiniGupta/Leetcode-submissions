class Solution:
    def maxArea(self, height: List[int]) -> int:
        # area=0
        # ans = 0
        # for i in range(len(height)):
        #     for j in range(i+1,len(height)):
        #         area= abs(min(height[i],height[j])*(i-j))
        #         ans = max(area, ans)
        # return ans
        left = 0
        right = len(height) - 1
        ans = 0
        while left<right:
            area = min(height[left],height[right])*(right-left)
            ans = max(area, ans)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return ans



        