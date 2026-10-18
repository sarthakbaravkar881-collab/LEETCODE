class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj=0
        count=0
        for i in nums:
            if count==0 and maj!=i:
                count+=1
                maj=i
            elif maj==i:
                count+=1
            else:
                count-=1
        return maj




