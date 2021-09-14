# The thought follows a simple rule:
# If the sum of a subarray is positive, it has possible to make the next value bigger, so we keep do it until it turn to negative.
# If the sum is negative, it has no use to the next element, so we break.
# it is a game of sum, not the elements.

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
                print('curSum to 0')
            curSum += n
            maxSub = max(maxSub, curSum)
            print('curSum: ', curSum)
            print('maxSub: ', maxSub, '\n')

        return maxSub

nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [-7,-6,-5,-4,-3,-2,1,3,4,1,2,1,-5,-4]
print('nums: ', nums)
sol = Solution()
print('sol:', sol.maxSubArray(nums) )

        # https://leetcode.com/problems/maximum-subarray/discuss/20396/Easy-Python-Way
        # MAXIMUM SUBARRAY - CODING INTERVIEW QUESTION
        # https://www.youtube.com/watch?v=5WZl3MMT0Eg 

        