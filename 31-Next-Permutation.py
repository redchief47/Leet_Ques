class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        i = len(nums) - 1
        j = i

        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1

        if i == 0:
            return nums.reverse()
        
        while j >= i and nums[j] <= nums[i -1]:
            j -= 1
        
        nums[i-1], nums[j] = nums[j], nums[i-1]

        nums[i:] = reversed(nums[i:])
            

        
