class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[0] < nums[mid] and (nums[left]>target or nums[right] > target):
                left = mid + 1
            elif nums[left] > target and nums[right] > target:
                left = mid + 1
            else:
                right = mid

        return left if left == right and nums[left] == target else -1