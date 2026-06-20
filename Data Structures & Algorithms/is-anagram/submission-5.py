class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s, count_t = {}, {}
        if len(s) != len(t):
            return False
        
        for l in range(len(s)):
            count_s[s[l]] = 1 + count_s.get(s[l], 0)
            count_t[t[l]] = 1 + count_t.get(t[l], 0)

        if count_s == count_t:
            return True
        else:
            return False
        