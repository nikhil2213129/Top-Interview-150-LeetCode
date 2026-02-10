class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 1
        sum = nums[0]
        minlen = 1000000
        while True:
            if sum<target:
                right += 1
                if right > len(nums):
                    break
                sum += nums[right-1]
            else:
                if right-left < minlen:
                    minlen = right - left
                left += 1
                sum -= nums[left-1]
        if minlen < 1000000:
            return minlen
        return 0
