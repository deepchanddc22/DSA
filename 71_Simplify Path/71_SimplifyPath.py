class Solution(object):
    def simplifyPath(self, path):

        components = path.split('/')
        stack = []

        for word in components:
            if word == '' or word == '.':
                continue
            elif word == "..":
                stack.pop()
            else:
                stack.append(word)

        return '/' + '/'.join(stack)

path = "/home/user/Documents/../Pictures"
sol = Solution()
print(sol.simplifyPath(path))