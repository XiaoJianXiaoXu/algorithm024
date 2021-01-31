#
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for i in range(0, len(nums)-1):
            if nums[i] != 0:
                if j != i:
                    nums[j] = nums[i]
                    nums[i] = 0
                j += 1

