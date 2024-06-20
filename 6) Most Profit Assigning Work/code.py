class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = sorted(zip(difficulty, profit))
        
       
        worker.sort()
        
        TotalProfit = 0
        best_profit = 0
        j = 0
        
        for ability in worker:
            while j < len(jobs) and ability >= jobs[j][0]:
              
                best_profit = max(best_profit, jobs[j][1])                                
                j += 1
           
            TotalProfit += best_profit
        
        return TotalProfit

difficulty = [68, 35, 52, 47, 86]
profit = [67, 17, 1, 81, 3]
worker = [92, 10, 85, 84, 82]

sol = Solution()
print(sol.maxProfitAssignment(difficulty, profit, worker))