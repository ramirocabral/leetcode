class Solution: 
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while True:
            num = numbers[left] + numbers[right]

            if num == target:
                return [left + 1, right + 1]
            if num > target:
                right -= 1
            else:
                left += 1
