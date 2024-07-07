class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        count = numBottles

        while numBottles>=numExchange:
              exch = numBottles//numExchange
              nonxch = numBottles%numExchange
              count = count + exch
              numBottles = exch + nonxch
            #   print(numBottles)
            #   print(count)
        return count
               




sol = Solution()
res = sol.numWaterBottles(numBottles=9,numExchange=3)
print(res)