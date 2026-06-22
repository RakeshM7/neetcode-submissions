class Solution:
    # using hash
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_hash, t_hash = {}, {}

        for char in s:
            if s_hash.get(char):
                s_hash[char] += 1
            else:
                s_hash[char] = 1

        for char in t:
            if t_hash.get(char):
                t_hash[char] += 1
            else:
                t_hash[char] = 1

        if s_hash.keys() != t_hash.keys():
            return False

        for char in s_hash.keys():
            if s_hash[char] != t_hash[char]:
                return False
        return True
        
        
