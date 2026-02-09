class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers)-1
        while left<=right:
            t = numbers[left]+numbers[right]
            if t == target:
                return list((left+1,right+1))
            if t > target:
                right -= 1
            if t < target:
                left += 1
        
