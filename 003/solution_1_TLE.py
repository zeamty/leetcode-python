class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        return max([j - i for i in range(0, len(s)) for j in range(i+1, len(s)+1) if (j - i) == len(set(s[i:j]))])
 
if __name__ == '__main__':
    print Solution().lengthOfLongestSubstring('abcabcbb') == 3
    print Solution().lengthOfLongestSubstring('bbbbb') == 1
    print Solution().lengthOfLongestSubstring('pwwkew') == 3
