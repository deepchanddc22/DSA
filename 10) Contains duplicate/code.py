class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_map = {}
        for num in nums:
            if num in num_map:
                return True
            num_map[num] = True
        return False

# Test cases
solution = Solution()
print(solution.containsDuplicate([1, 2, 3, 1]))  # Output: True
print(solution.containsDuplicate([1, 2, 3, 4]))  # Output: False
print(solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # Output: True
