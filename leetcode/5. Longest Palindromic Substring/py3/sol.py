class Solution:
    def isPalindrome(self, ins):
      sub = ins[1:-2]
      print('sub: ', sub)
      if ins[0] == ins[-1] and self.isPalindrome(sub):
        return True
      else:
        return False

    def longestPalindrome(self, s: str) -> str:
      ret = self.isPalindrome(s)
      print('ret: ', ret)


s = "cbbd"
sol = Solution()
ret = sol.longestPalindrome(s)
