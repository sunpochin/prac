# import math

class Solution:
  def longestConsecutive(self, nums):
    if not nums:
      return 0

    # use set to filter out repeated 1 in case [0, 1, 1, 2]
    setNums = set(nums)
    print('setNums: ', setNums)
    nums = []
    for it in setNums:
      nums.append(it)
    # sort the filtered new array.
    nums.sort()
    print('newnums sorted: ', nums)
    # consecutive number set to 1 for only one element.
    curcon = 1
    maxcon = 0
    for it in range(len(nums)):
      if it == 0:
        curcon = 1
        continue

      delta = nums[it] - nums[it-1]
      print('delta: ', delta)
      if (1==delta):
        curcon += 1
      else:
        # if end of streak, set maxcon to new max.
        maxcon = max(maxcon, curcon)
        print('maxcon: ', maxcon)
        curcon = 1

    # end of for loop,
    maxcon = max(maxcon, curcon)
    print('maxcon: ', maxcon)
    curcon = 1
    return maxcon


testcase = [1,2,0,1]
sol = Solution()
ret = sol.longestConsecutive(testcase)

print('nums: ', ret)

