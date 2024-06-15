class Solution(object):
    def minIncrementForUnique(self, nums):
        nums.sort()  
        moves = 0
        
      
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                increment = nums[i - 1] - nums[i] + 1
                nums[i] += increment
                moves += increment
        
        return moves


nums = [3, 2, 1, 2, 1, 7]
Sol = Solution()
print(Sol.minIncrementForUnique(nums))  