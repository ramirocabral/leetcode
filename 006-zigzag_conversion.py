class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = ['' for _ in range(numRows)]
        if (numRows == 1) : return s
        pos = 0
        while pos < len(s):
            i = 0
            while ((i < numRows) and (pos < len(s))):
                rows[i] = rows[i] + s[pos]
                pos = pos + 1
                i = i + 1
            j = numRows - 1 - 1
            while (j>=1 and pos < len(s)):
                rows[j] = rows[j] + s[pos]
                pos = pos + 1
                j = j-1

        return ''.join(rows)
