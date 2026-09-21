class Solution:
    def twoSum(self,nums,target):
        hash_map = {}
        for i,n in enumerate(nums):
            A = target - nums[i]
            if A in hash_map:
                return [hash_map[A], i]
            hash_map[n] = i
        return []

    
        