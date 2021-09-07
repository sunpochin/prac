from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        theSet = set()
        for it in nums:
          if it in theSet:
            theSet.remove(it)
          else:
            theSet.add(it)

        print('the Set: ', theSet)
        ans = theSet.pop()
        return ans

sol = Solution()
inp = [2,2,1,1,3,3,4]
ret = sol.singleNumber(inp)
print('ret: ', ret)


