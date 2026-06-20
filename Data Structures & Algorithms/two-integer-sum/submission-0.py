class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n in range(len(nums)):
            first = nums[n]
            for j in range(len(nums)):
                if n == j:
                    continue
                else:
                    if target == first + nums[j]:
                        return [n,j]

        