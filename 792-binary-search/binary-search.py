class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=0
        e=len(nums)-1
        while l<=e:
            mid=l+(e-l)//2
            if target>nums[mid]:
                l=mid+1
            elif nums[mid]>target:
                e=mid-1
            else:
                return mid
        return -1