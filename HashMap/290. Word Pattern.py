class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        if len(pattern) != len(words):
            return False

        d = {}
        e = {}
        for p, w in zip(pattern, words):
            if p in d:
                if d[p] != w:
                    return False
            else:
                if w in e:
                    return False
                d[p] = w
                e[w] = p
        return True
