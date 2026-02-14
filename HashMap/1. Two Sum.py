class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}
        for i in range(len(nums)):
            current = nums[i]
            x = target - current
            if x in num_map:
                return [num_map[x], i]
            else:
                num_map[current] = i  
        


        
