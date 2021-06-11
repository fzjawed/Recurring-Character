class Solution:
    def solve(self, s):
        l = []
        if len(s) > 1:
            for i in range(len(s)):
                if s[i] not in l:
                    l.append(s[i])
                else:
                    recurring = i
                    break
            if len(set(l)) == len(s):
                return -1
            else:
                return recurring
        else:
            return -1