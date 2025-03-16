class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]

        num_map = {}

        for num in nums:
            num_map[num] = 1 + num_map.get(num, 0)

        for n, count in num_map.items():
            freq[count].append(n)

        res = []

        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
