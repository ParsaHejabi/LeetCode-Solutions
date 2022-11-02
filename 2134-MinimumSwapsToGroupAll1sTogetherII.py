from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones_quantity = 0
        for i in range(len(nums)):
            ones_quantity += nums[i]

        window_start = 0
        window_end = window_start + ones_quantity - 1

        max_ones_in_window = 0
        for i in range(window_start, window_end + 1):
            max_ones_in_window += nums[i]

        current_ones_in_window = max_ones_in_window
        while window_start < len(nums) - 1:
            current_ones_in_window -= nums[window_start]
            window_start += 1
            window_end += 1
            current_ones_in_window += nums[window_end % len(nums)]

            if current_ones_in_window > max_ones_in_window:
                max_ones_in_window = current_ones_in_window

        return ones_quantity - max_ones_in_window
