class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2:
            return s
        l = [''] * numRows
        index, step = 0, 1
        for x in s:
            l[index] += x
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return ''. join(l)

print Solution().convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
print Solution().convert('123456789012', 4)
print Solution().convert('', 1)
print Solution().convert('abcde', 5)
