class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_neg = x < 0
        x = abs(x)
        r = 0
        while x > 0:
            r = r * 10 + x % 10
            x = x / 10
        if r >= 2 ** 31:
            r = 0
        return r * -1 if is_neg else r

print Solution().reverse(123) == 321
print Solution().reverse(-123) == -321
print Solution().reverse(120) == 21
print Solution().reverse(0) == 0
print Solution().reverse(1534236469) == 0
print Solution().reverse(-2147483412) == -2143847412
