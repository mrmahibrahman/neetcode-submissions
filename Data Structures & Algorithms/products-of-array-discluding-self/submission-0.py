class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # This the idea, for every index i, we want 
        # product of everything to left of i, and product of everything to right of i

        '''
        ex: nums = [1,2,3,4]

        index 2 = 3

        left product = 1*2 = 2
        right product = 4
        answer = 8
        '''
        
        # Create a result array [1,1,1,1]
        res = [1] * (len(nums))

        # prefix is the product of all numbers BEFORE current inex
        prefix = 1
        #[1,2,3,4]
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # [1,1,2,6]
        # [,48,24,6]
        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res