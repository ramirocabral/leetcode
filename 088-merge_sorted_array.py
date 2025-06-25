class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i = m+n-1
        index2 = n-1
        index1 = m-1
        while index1 >= 0 and index2 >= 0:
            if (nums2[index2] >= nums1[index1]):
                nums1[i] = nums2[index2]
                index2 -= 1
            else:
                nums1[i] = nums1[index1]
                index1 -= 1

            i -= 1

        while index1 >= 0:
            nums1[i] = nums1[index1]
            index1 -= 1
            i-=1

        while index2 >= 0:
            nums1[i] = nums2[index2]
            index2 -= 1
            i-=1
