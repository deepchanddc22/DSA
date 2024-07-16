class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        arr = []
        new_num = 0

        while num > 0:
            remainder = num % 2
            arr.append(remainder)
            num = num // 2

        arr.reverse()

        for i in range(len(arr)):
            if arr[i] == 1:
                arr[i] = 0
            else:
                arr[i] = 1
        # return arr

        arr.reverse() 
    
        for j in range(len(arr)):
            new_num = new_num + 2**j*arr[j]

        return new_num

    

        
sol = Solution()
print(sol.findComplement(num=2))