class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts1 = {}
        counts2 = {}
        for ch in s:
            if ch not in counts1:
                counts1[ch] = 1
            else:
                counts1[ch] += 1
        for ch in t:
            if ch not in counts2:
                counts2[ch] = 1
            else:
                counts2[ch] += 1
        for key in counts1:
            if key not in counts2:
                return False
            if counts1[key] != counts2[key]:
                return False
        return True
