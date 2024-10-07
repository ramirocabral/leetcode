class Solution:
    def reverse(self, x: int) -> int:
        aux = abs(x)
        number = 0
        while (aux > 0):
            digit = aux % 10
            aux = aux // 10
            number = number * 10 + digit

        if (x<0):
            number = number * (-1)

        if ((number < -(2**31)) or (number > (2**31) -1)):
            return 0

        return number
