from typing import List


class Solution:
    def merge(self, arr1: List[int], arr2: List[int]) -> List[int]:
        merged_arr = []
        arr1_index = 0
        arr2_index = 0

        while arr1_index < len(arr1) and arr2_index < len(arr2):
            merged_arr.append(min(arr1[arr1_index], arr2[arr2_index]))

        if arr1_index < len(arr1):
            while arr1_index < len(arr1):
                merged_arr.append(arr1[arr1_index])
        elif arr2_index < len(arr2):
            while arr2_index < len(arr2):
                merged_arr.append(arr2[arr2_index])

        return merged_arr

    def divide(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                temp = nums[0]
                nums[0] = nums[1]
                nums[1] = temp
        elif len(nums) == 3:
            min_val = math.inf
            min_index = None
            max_val = -math.inf
            max_index = None
            for i in range(3):
                if nums[i] > max_val:
                    max_val = nums[i]
                    max_index = i

                if nums[i] < min_val:
                    min_val = nums[i]
                    min_index = i

            if min_index == max_index:
                return nums
            else:
                avg_index = 3 - min_index - max_index
                return [nums[min_index], nums[avg_index], nums[max_index]]

        mid = len(nums) // 2
        left_part = self.divide(nums[:mid])
        right_part = self.divide(nums[mid:])

        return merge(left_part, right_part)

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.divide(nums)
