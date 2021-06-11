#creds to cryptic_dagger on binarysearch
class Solution:
    def solve(self, s):
        a = set()
        n = min(len(s), 27)
        for i in range(n):
            if s[i] in a:
                return i
            else:
                a.add(s[i])
        return -1