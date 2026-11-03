class Solution:
    def minMoves(self, nums: List[int]) -> int:
        tar = max(nums)                  # target = largest element
        count = 0
        for i in range(len(nums)):       # loop over indexes, not over a value
            while nums[i] < tar:         # < instead of <=
                nums[i] = nums[i] + 1    # raise the element, not the target
                count = count + 1
        return count