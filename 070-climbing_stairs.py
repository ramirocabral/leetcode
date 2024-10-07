class Solution:
    def climbStairs(self, n: int) -> int:

        @cache
        def climb(n) :
            if (n==1):
                return 1
            elif (n==2):
                return 2
            return climb(n-1) + climb(n-2)
        return climb(n
