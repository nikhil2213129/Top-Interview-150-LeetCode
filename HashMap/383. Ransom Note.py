class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        m = {}
        for i in magazine:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1
        for j in ransomNote:
            if j in m:
                if m[j] > 0:
                    m[j] -= 1
                else:
                    return False
            else:
                return False
        return True
