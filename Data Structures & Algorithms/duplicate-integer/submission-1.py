class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for i2 in range(len(nums)):
                if nums[i] == nums[i2] and i != i2:
                    return True
        return False