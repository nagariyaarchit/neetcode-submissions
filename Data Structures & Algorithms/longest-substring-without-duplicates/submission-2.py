class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_so_far = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_so_far:
                char_so_far.remove(s[left])
                left += 1

            char_so_far.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length