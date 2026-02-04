class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        r = len(nums) - k
        new = nums[0:r]
        nums[0:r] = []
        nums.extend(new)
