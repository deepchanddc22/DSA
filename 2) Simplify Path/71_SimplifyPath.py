class Solution(object):
    def simplifyPath(self, path):

        components = path.split('/')
        stack = []

        for word in components:
            if word == '' or word == '.':             
                continue                
            elif word == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(word)

        return '/' + '/'.join(stack)

path = "/home/user/Documents/../Pictures"
sol = Solution()
print(sol.simplifyPath(path))

'''Concepts to learn
1) Use of Stack
2) .join() method'''