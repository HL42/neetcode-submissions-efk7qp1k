class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [0] * (2 * length)
        for i in range(0, length):
            result[i] = nums[i]
            result[i + length] = nums[i]

        
        return result
        