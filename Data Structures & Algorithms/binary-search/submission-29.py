class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            potential = nums[m]

            if (potential == target):
                return m

            if potential > target: 
                r = m - 1
            elif potential < target:
                l = m + 1 

        return -1