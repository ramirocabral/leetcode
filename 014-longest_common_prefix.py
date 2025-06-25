class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]

        for i in range (1, len(strs)):
            aux = strs[i]

            end = len(aux) if len(prefix) > len(aux) else len(prefix)
            new_prefix = ""

            for j in range (0, end):
                char = prefix[j]
                if (char == aux[j]):
                    new_prefix += char
                else:
                    break

            prefix = new_prefix

        return prefix
