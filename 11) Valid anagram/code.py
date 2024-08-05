class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_freq = {}
        t_freq = {}

        for schar in s:
            if schar in s_freq:
                s_freq[schar] += 1
            else:
                s_freq[schar] = 1


        for tchar in t:
            if tchar in t_freq:
                t_freq[tchar] += 1
            else:
                t_freq[tchar] = 1


        if s_freq == t_freq:
            return True
        else:
            return False


        


sol = Solution()
s = "anagram"
t = "nagaram"

print(sol.isAnagram(s,t))