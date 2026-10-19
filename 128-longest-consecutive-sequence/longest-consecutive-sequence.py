class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        count=1
        longest=1
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            elif nums[i-1]==nums[i]-1:
                count+=1
            else:
                longest=max(longest,count)
                count=1
            
        return max(count,longest)
