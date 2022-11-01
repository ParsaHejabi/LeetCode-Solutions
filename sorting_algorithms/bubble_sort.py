from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    temp = nums[j + 1]
                    nums[j + 1] = nums[j]
                    nums[j] = temp
        return nums


if __name__ == '__main__':
    arr = [6, 3, 8, 1, 9, 15, 0]
    arr2 = [1]
    solution = Solution()
    print(solution.sortArray(arr))
    print(solution.sortArray(arr2))
