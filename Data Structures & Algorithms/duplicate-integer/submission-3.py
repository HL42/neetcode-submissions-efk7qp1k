class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hashset = set()

        for temp in nums:
            if temp in hashset:
                return True
            hashset.add(temp)

        return False

                

        