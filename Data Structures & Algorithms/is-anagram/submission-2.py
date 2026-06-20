class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for l in s:
            if l not in t or s.count(l) != t.count(l):
                return False
        
        for l in t:
            if l not in s or t.count(l) != s.count(l):
                return False
        return True
