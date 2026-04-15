class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nums.sort()
        arr_len = len(nums)

        for i in range(0, arr_len - 1):
            if nums[i] == nums[i+1]:
                return True


        return False

                

        