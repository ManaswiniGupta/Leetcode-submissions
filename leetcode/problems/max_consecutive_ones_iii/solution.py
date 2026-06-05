class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        right=0
        ans=0
        if not nums:
            return 0
         # Safe initial tracking for the very first element
        if nums[0] == 1:
            ans = 1
        elif nums[0] == 0 and k > 0:
            ans = 1
            k -= 1
        else:
            # If the first element is 0 and k is 0, window starts empty
            left = 1
            right = 0

         
        curr= nums[left:right+1]   
        while right<len(nums)-1:
            new_char =  nums[right+1]
            if new_char==1:
                right+=1
                curr=nums[left:right+1]
                
                ans=max(ans, len(curr))
            else:
                if k!=0:
                    right+=1
                    curr = nums[left:right+1]
                    k -= 1
                    ans = max(ans, len(curr))
                else:
                     # PATCH: If window has elements, shrink left to reclaim a flip
                    if left <= right:
                        if nums[left] == 0:
                            k += 1
                        left += 1
                        curr = nums[left:right+1]
                    else:
                        # PATCH: If window is empty and k=0, skip this zero entirely
                        right += 1
                        left = right + 1
                        curr = nums[left:right+1]
        return ans