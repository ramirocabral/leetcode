class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for st in strs:
            letters = {}
            for char in st:
                letters[char] = 1 + letters.get(char, 0)

            key = tuple(sorted(letters.items()))

            if key not in result:
                result[key] = []
            result[key].append(st)

        return list(result.values())
