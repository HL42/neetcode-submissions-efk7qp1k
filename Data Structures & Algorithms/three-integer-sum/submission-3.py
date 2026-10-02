class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ## nums[i] = -nums[j] - nums[k]
        nums.sort()
        result = []


        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1 

            while left < right:
                num = nums[i] + nums[left] + nums[right]

                if num == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif num > 0:
                    ## 数组由小到大排序 如果总和大于0我们希望大的数变小
                    right -= 1
                elif num < 0:
                    left += 1

        return result


