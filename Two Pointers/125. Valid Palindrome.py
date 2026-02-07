class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ch = ""
        for i in s:
            if i.isalnum():
                ch += i.lower()
        ptr1 = 0
        ptr2 = len(ch)-1
        while ptr1<=ptr2:
            if ch[ptr1] != ch[ptr2]:
                return False
            ptr1 += 1
            ptr2 -= 1
        return True
