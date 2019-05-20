class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices)==0:
            return 0
        opt =[0]*len(prices)
        for i in range(1,len(prices)):
            opt[i] = max(opt[i-1]+prices[i]-prices[i-1],0)
        print(opt)
        return max(opt)

    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        length = len(cost)
        dp = 0
        a = cost[0]
        b = cost[1]
        for i in range(2, length):
            dp = cost[i] + min(a, b)
            a = b
            b = dp
        return min(a,b)

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        res = [0] * len(nums)
        res[0] = nums[0]
        for i in range(1, len(nums)):
            res[i] = max(res[i-1] + nums[i], nums[i])

        return max(res)

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0

        for i in nums: last, now = now, max(last + i, now)

        return now

    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) <= 2:
            return 0
        length = len(A)
        dp = [0 for _ in range(length)]
        for i in range(2, len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i] = dp[i-1] + 1
        return sum(dp)
