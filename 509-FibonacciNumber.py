class Solution:
    def fib(self, n: int) -> int:
        bottom_up = []
        bottom_up.append(1)
        bottom_up.append(1)

        if n == 0:
            return 0

        if n == 1 or n == 2:
            return 1

        for i in range(2, n):
            bottom_up.append(bottom_up[i-1] + bottom_up[i-2])

        return bottom_up[n-1]
