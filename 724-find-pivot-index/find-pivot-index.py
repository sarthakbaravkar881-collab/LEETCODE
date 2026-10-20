class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftsum=0
        total=sum(nums)
        for i in range (len(nums)):
            rightsum=total-nums[i]-leftsum
            if rightsum==leftsum:
                return i
            else:
                leftsum=leftsum+nums[i]
        return -1