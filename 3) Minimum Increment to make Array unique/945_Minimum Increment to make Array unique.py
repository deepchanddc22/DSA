class Solution(object):
    def minIncrementForUnique(self, nums):
        nums.sort()  # Step 1: Sort the array
        moves = 0
        
        # Step 2: Iterate and fix duplicates
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                increment = nums[i - 1] - nums[i] + 1
                nums[i] += increment
                moves += increment
        
        return moves

# Example usage:
nums = [3, 2, 1, 2, 1, 7]
Sol = Solution()
print(Sol.minIncrementForUnique(nums))  # Output: 6
