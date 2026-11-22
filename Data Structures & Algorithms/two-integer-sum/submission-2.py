class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(0, length):
            unique = set(nums[i+1:])
            otherpart = target - nums[i]
            if otherpart in unique:
                for j in range(i+1, length):
                    if otherpart == nums[j]:
                        return [i, j]

            

        