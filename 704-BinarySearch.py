class Solution:
    def binary_search_recursive(self, nums: List[int], left: int, right: int, target: int) -> int:
        if left > right:
            return -1

        mid = left + ((right - left) // 2)

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binary_search_recursive(nums, left, mid - 1, target)
        else:
            return self.binary_search_recursive(nums, mid + 1, right, target)

    def search(self, nums: List[int], target: int) -> int:
        recursive = False
        if recursive:
            return self.binary_search_recursive(nums, 0, len(nums) - 1, target)
        else:
            left = 0
            right = len(nums) - 1

            while (left <= right):
                mid = left + ((right - left) // 2)
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return -1
