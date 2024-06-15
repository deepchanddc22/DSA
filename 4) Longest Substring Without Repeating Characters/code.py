class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_index_map = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            if s[right] in char_index_map and char_index_map[s[right]] >= left:      
                left = char_index_map[s[right]] + 1
            
            char_index_map[s[right]] = right
            max_length = max(max_length, right - left + 1)
        
        return max_length


s = "abddcf"
if len(s) > 0:
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))
else:
    print(0)
