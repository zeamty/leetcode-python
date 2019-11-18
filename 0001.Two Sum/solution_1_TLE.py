class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [[a, b] for a in range(0, len(nums)) for b in range(a + 1, len(nums)) if nums[a] + nums[b] == target][0]
        
if __name__ == '__main__':
    print Solution().twoSum([3,2,4], 6)
