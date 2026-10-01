class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hash_set = set(nums)
        total_count = 0

        for num in nums:
            if num - 1 not in hash_set:

                current_value = num
                current_count = 1

                while current_value + 1 in hash_set:
                    current_value += 1
                    current_count += 1

                total_count = max(total_count, current_count)

        return total_count