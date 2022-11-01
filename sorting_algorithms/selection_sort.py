from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            min_index = i
            for j in range(i, len(nums)):
                if nums[j] < nums[min_index]:
                    min_index = j

            temp = nums[i]
            nums[i] = nums[min_index]
            nums[min_index] = temp
        return nums


if __name__ == '__main__':
    arr = [6, 3, 8, 1, 9, 15, 0]
    arr2 = [1]
    solution = Solution()
    print(solution.sortArray(arr))
    print(solution.sortArray(arr2))
