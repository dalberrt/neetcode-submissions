class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        chat = set()
        for n in nums:
            if n in chat:
                return True
            chat.add(n)
        return False