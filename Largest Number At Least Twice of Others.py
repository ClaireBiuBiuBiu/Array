class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m = max(nums)
        if all(m >= 2 * n for n in nums if n != m):
            return nums.index(m)

        return -1
