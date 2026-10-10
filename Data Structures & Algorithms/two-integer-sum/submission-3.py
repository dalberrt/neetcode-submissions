class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        test = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i]+nums[j] == target:
                    test.append(i)
                    test.append(j)
                    break
            if test != []:
                break
        return test
                
