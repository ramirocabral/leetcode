class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for left, left_val in enumerate(nums):
            mid = left + 1
            right = len(nums) - 1

            ## we can no longer sum 0
            if left_val > 0:
                break

            if left > 0 and left_val == nums[left - 1]:
                continue

            while mid < right:
                mid_val = nums[mid]
                right_val = nums[right]
                sum = left_val + mid_val + right_val
                if sum == 0:
                    res.append([left_val, mid_val, right_val])
                    mid += 1
                    right -= 1
                    while mid < right and nums[mid] == nums[mid - 1]:
                        mid += 1
                    continue
                if sum < 0:
                    mid += 1
                else:
                    right -= 1

        return res
