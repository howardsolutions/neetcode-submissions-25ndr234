class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = cnt = 0 

        for i in range(len(nums)):
            if nums[i] == 1: 
                cnt += 1
            else:
                res = max(cnt, res)
                cnt = 0
            
        return max(cnt, res)