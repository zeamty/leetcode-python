class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ele_pos_dict = {}
        max_len = 0 
        i = 0 
        j = 0 
        len_s = len(s)
        while j < len_s:
            if s[j] not in ele_pos_dict or ele_pos_dict[s[j]] < i:
                ele_pos_dict[s[j]] = j 
            else:
                max_len = max(max_len, (j-i))
                i = ele_pos_dict[s[j]] + 1 
                ele_pos_dict[s[j]] = j 
            j += 1
        return max(max_len, (j-i))

if __name__ == '__main__':
    print Solution().lengthOfLongestSubstring('abcabcbb') == 3
    print Solution().lengthOfLongestSubstring('bbbbb') == 1
    print Solution().lengthOfLongestSubstring('pwwkew') == 3
    print Solution().lengthOfLongestSubstring('abba') == 2
