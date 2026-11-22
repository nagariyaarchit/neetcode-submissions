class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        solution_array = []
        length = len(nums)
        prefix = 1
        for i in range (0, length):
            solution_array.append(prefix)
            prefix *= nums[i]

        suffix = 1
        for i in range(length - 1, -1, -1):
            solution_array[i] *= suffix
            suffix *= nums[i]

        return solution_array

        
        