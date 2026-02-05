class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # create a pointer at index 0
        # check the value at index
        # if the value >0 move, increase pointer
        # if pointer == len(nums)-1, return True
        # else: return False
        ptr = 0
        for i in range(len(nums)):
            if i>ptr:
                return False
            ptr = max(ptr,i+nums[i])
        return True

