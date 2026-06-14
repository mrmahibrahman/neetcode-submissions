class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Step 1: Use a nested for loop to add up one element to each element in the list of nums

        # Step 2: If sum of two elements is equal to the target, do step 3

        # Step 3: return a list of indices where the two sum is equal to the target

        total = 0
        indices = []

        # Step 1: 
        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if i != j + 1: 
                    total = nums[i] + nums[j + 1]

                # step 2
                if total == target:
                    indices.append(i)
                    indices.append(j + 1)

                    # step 3
                    return indices
                else: 
                    total = 0


                
        