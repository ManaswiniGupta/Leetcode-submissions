class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = 0  # Start pointer
        e = 1  # End pointer
        
        while s < len(nums):  # Ensure 's' stays within bounds
            if e >= len(nums):  # Reset 'e' and move 's' forward
                s += 1
                e = s + 1
                continue
            
            # Check if the sum equals the target
            if nums[s] + nums[e] == target:
                return [s, e]
            
            # Increment 'e' to check the next pair
            e += 1
        
        return []