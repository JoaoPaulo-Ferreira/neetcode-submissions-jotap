class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = defaultdict(int)
        for l in s:
            letters[l] += 1
        for l in t:
            letters[l] -= 1
        for key,val in letters.items():
            if val != 0:
                return False
        return True

