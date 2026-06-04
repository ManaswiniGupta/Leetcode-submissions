class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # 1. Compute the sum of the very first window of size k
        current_window_sum = sum(nums[:k])
        max_window_sum = current_window_sum
        
        # 2. Slide the window across the rest of the array
        for i in range(k, len(nums)):
            # Add the incoming element (nums[i]) and subtract the outgoing element (nums[i - k])
            current_window_sum += nums[i] - nums[i - k]
            
            # Keep track of the highest sum found so far
            max_window_sum = max(max_window_sum, current_window_sum)
            
        # 3. Divide by k at the very end to get the maximum average
        return max_window_sum / k
