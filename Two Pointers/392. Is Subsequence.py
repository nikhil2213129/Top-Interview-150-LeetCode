class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sptr = 0
        tptr = 0
        while sptr<len(s) and tptr<len(t):
            if s[sptr] == t[tptr]:
                sptr += 1
            tptr += 1
        return sptr == len(s)
