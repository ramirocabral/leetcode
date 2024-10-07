class Solution:
    def longestPalindrome(self, s: str) -> str:
        if (len(s) <= 1) : return s

        max_string = ""
        max_length = 1
        for i in range(0,len(s) - 1):
            curr_length = 1
            step = 1
            while ((i-step) >= 0 and (i+step) < len(s) and s[i-step] == s[i+step]):
                curr_length = curr_length + 2
                step = step + 1

            if (curr_length > max_length):
                max_string = s[i-step+1:i+step]
                max_length = curr_length

            # no quiero pensar
            if(s[i+1] == s[i]):
                curr_length = 2
                step = 1
                while ((i-step)>=0 and (i+step+1)<len(s) and (s[i-step] == s[i+step+1])):
                    curr_length = curr_length + 2
                    step = step + 1

            if (curr_length > max_length):
                max_string = s[i-step+1:i+step+1]
                max_length = curr_length

        if (max_length == 1):
            return s[0]

        return max_string
