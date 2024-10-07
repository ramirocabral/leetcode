class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if (len(nums) == 1):
            curr_pos = 0
        else:
            curr_pos = 1
            while (curr_pos < len(nums)-1 and nums[curr_pos] >= nums[curr_pos]-1):
                curr_pos = curr_pos + 1
    
        while ((min_pos := self.findMinimumGreatherThan(nums,nums[curr_pos],curr_pos)) == -1 and curr_pos > 0):
            curr_pos = curr_pos - 1

        if (curr_pos == 0 and min_pos == -1):
            if (len(nums) > 1):
                min_pos = nums.index(min(nums[1:]))

        self.swap(nums,curr_pos,min_pos)

        #ordenar desde la posicion swapeada
        for i in range(curr_pos+1, len(nums) - 1):
            for j in range(curr_pos+1, len(nums) - i + curr_pos ):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

    def findMinimumGreatherThan(self,list, value, pos):
        greater = [(i, x) for i, x in enumerate(list[pos:], start=pos) if x > value]
        
        if greater:
            index_min, _ = min(greater, key=lambda x: x[1])
            return index_min
        else:
            return -1 
       
    def swap(self, nums, index1,index2) -> None:
        aux = nums[index1]
        nums[index1] = nums[index2]
        nums[index2] = aux
