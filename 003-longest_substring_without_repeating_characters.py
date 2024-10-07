class Solution:
    def lengthOfLongestSubstring(self, s:str) -> int:
        curr_string = ""
        longest_string = ""
        for c in s:
            if curr_string.count(c) > 0:
                curr_string = curr_string[curr_string.find(c) + 1:]
            curr_string += c
            if len(curr_string) > len(longest_string):
                longest_string = curr_string

        return len(longest_string)
