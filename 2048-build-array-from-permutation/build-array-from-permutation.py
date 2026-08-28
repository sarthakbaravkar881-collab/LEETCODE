class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n=nums.copy()
        for i in range (len(nums)):
            nums[i]=n[n[i]]
        return nums