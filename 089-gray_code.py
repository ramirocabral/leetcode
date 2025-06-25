class Solution:
    def grayCode(self, n: int) -> list[int]:
        # 8 = 1000 -> 1100
        # 7 = 0111 -> 0100
        # 6 = 0110 -> 0101
        # 5 = 0101 -> 0111
        # 4 = 0100 -> 0110
        # gray_code[i] = i ^ (i >> 1)
        list = []
        for i in range(2**n):
            list.append(i ^ (i >> 1))

        return list
