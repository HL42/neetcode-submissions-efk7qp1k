class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n == 1:
            return nums[0]

        case1 = self.rob1(nums[:-1])

        case2 = self.rob1(nums[1:])

        return max(case1, case2)

        

    def rob1(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [0] * (n + 1)

        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums[0], nums[1])

        dp[1] = nums[0]
        dp[2] = max(nums[0], nums[1])

        
        for i in range(3, n + 1):
            dp[i] = max(nums[i - 1] + dp[i - 2], dp[i - 1])


        return dp[n]