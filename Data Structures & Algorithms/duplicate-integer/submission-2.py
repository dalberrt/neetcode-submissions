class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        chat = []
        for n in nums:
            if n in chat:
                return True
            chat.append(n)
        return False