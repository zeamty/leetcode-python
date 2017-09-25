class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for a in range(0, length):
            for b in range(a+1, length):
                if nums[a] + nums[b] == target:
                    return [a, b]
        
if __name__ == '__main__':
    print Solution().twoSum([3,2,4], 6)
