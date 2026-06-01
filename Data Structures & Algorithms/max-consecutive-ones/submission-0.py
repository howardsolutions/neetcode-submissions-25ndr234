class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = cnt = 0 
        for i in range(len(nums)):
            if nums[i] == 0:
                res = max(cnt, res)
                cnt = 0 
            else:
                cnt += 1
        
        return max(res, cnt)