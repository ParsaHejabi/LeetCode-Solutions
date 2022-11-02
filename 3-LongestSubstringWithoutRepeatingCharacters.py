class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring_length = 0
        hash_table = {}
        window_start = 0

        for window_end in range(len(s)):
            if s[window_end] in hash_table.keys():
                hash_table[s[window_end]] += 1
                while hash_table[s[window_end]] > 1:
                    hash_table[s[window_start]] -= 1
                    window_start += 1
                    if hash_table[s[window_start]] == 0:
                        del hash_table[s[window_start]]
                if window_end - window_start + 1 > longest_substring_length:
                    longest_substring_length = window_end - window_start + 1
            else:
                hash_table[s[window_end]] = 1
                if window_end - window_start + 1 > longest_substring_length:
                    longest_substring_length = window_end - window_start + 1

        return longest_substring_length
