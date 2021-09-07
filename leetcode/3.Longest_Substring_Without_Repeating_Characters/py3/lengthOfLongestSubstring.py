# https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/742926/Simple-Explanation-or-Concise-or-Thinking-Process-and-Example

# https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/347818/Python3%3A-sliding-window-O(N)-with-explanation



class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int abcabcbb
        """
        if len(s) == 0:
            return 0

        seen = {}
        left, right = 0, 0
        longest = 1
#        print('right: ', right, ', len(s): ', len(s) )
        while right < len(s):
#            print('s[right]: ', s[right], ', seen: ', seen)
            if s[right] in seen:
#                left = seen[s[right]] + 1
                left = max(left, seen[s[right]] + 1)
            longest = max(longest, right - left + 1)
#            print('right: ', right, ', left: ', left, 'longest: ', longest, ', crop: ',            s[left:right+1])
            seen[s[right]] = right
            right += 1
        return longest

# s = "pwwkew"
s = "abba"
sol = Solution()
ret = sol.lengthOfLongestSubstring(s)
print('ret: ', ret)

