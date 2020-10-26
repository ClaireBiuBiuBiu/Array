'''
Given an array of integers nums,
 write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of all the numbers to
the left of the index is equal to the sum of all the numbers to the right of the index.

If no such index exists, we should return -1.
If there are multiple pivot indexes, you should return the left-most pivot index.
'''
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        leftsum = 0
        for i,n in enumerate(nums):
            if leftsum == s-n-leftsum:
                return i #这里避开了思考里面有几个 因为但凡遇到第一个 已经返回了，没遇到就自动第二次
            leftsum += n #没遇到就叠加
        return -1