class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prev_map = {}

        for i, n in enumerate(nums):
            j = target - n


            if j in prev_map:
                return [prev_map[j],i]

            
            prev_map[n] = i