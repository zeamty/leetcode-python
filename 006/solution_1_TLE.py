class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2:
            return s
        patch_n = (numRows * 2 - 2)
        cols = len(s) / patch_n * (numRows - 1)
        rest = len(s) - cols / (numRows - 1) * patch_n
        if rest > 0:
            cols += 1
            rest -= numRows
            if rest > 0:
                cols += rest
    
        d = [['' for x in range(0, numRows)] for y in range(0, cols)]
        for i, x in enumerate(s):
            a = i / patch_n
            b = i % patch_n
            if b < numRows:
                d[a*(numRows-1)][b] = x
            else:
                d[a*(numRows-1)+b-numRows+1][numRows-(b-numRows)-2] = x

        ret = ''
        for j in range(0, numRows):
            for i in range(0, cols):
                ret += d[i][j]
        return ret
print Solution().convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
print Solution().convert('123456789012', 4)
print Solution().convert('', 1)
print Solution().convert('abc', 1)
