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

        # total = 0
        # indices = []

        # # Step 1: 
        # for i in range(len(nums)):
        #     for j in range(len(nums) - 1):
        #         if i != j + 1: 
        #             total = nums[i] + nums[j + 1]

        #         # step 2
        #         if total == target:
        #             indices.append(i)
        #             indices.append(j + 1)

        #             # step 3
        #             return indices
        #         else: 
        #             total = 0


        # Step 1: Create a dictionary/hash map that stores key as the number, and the value is the index

        # Step 2: We know the target, so that means we can find the difference between
        # target - the element to find the other

        # Step 3: if the number of the difference is equal to the number in the dictionary, we found our match!
        
        num_values = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in num_values:
                return [num_values[diff], i]
            
            num_values[nums[i]] = i









                
        