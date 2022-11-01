from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            curr = nums[i]
            corr_index = i
            for j in range(i - 1, -1, -1):
                if curr < nums[j]:
                    nums[j + 1] = nums[j]
                    corr_index = j
                else:
                    corr_index = j + 1
                    break

            nums[corr_index] = curr
        return nums


if __name__ == '__main__':
    arr = [6, 3, 8, 1, 9, 15, 0]
    arr2 = []
    arr3 = [1]
    solution = Solution()
    print(solution.sortArray(arr))
    print(solution.sortArray(arr2))
    print(solution.sortArray(arr3))
