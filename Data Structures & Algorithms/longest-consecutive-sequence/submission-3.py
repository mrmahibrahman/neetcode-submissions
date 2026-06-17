class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Input: nums = [2,20,4,10,3,4,5]

        Output: 4

        [2,3,4,5]

        map[n - 1] == true

        We are gonna use hashset

        Step 1: lets put all the nums in the hashet (key is the number)

        Step 2: Lets go through each number in the array, for each number, check, 
        does a left position exist by subtracting 1? If yes, we know this is not the start of the sequence
        and we continue. 
        
        -If not, this is the start of the sequence. If this is a start of the sequence, check if theres a right position in the set. If yes, add to the sequence

        Step 3: take the length of solution and output that

        so a sequence is like this
        we have [100, 4, 200, 1, 3, 2]

        so one sequence is: 1,2,3,4 (length 4)
        another sequence is: 100
        last sequence is: 200

        How do we know to start a beginning a sequence, start value for the first range 1 does not have a left neighbor, 100 does not have a left neighbor

        does the array contain 
        Ex: 100: does 99 exist in the array? NO. Does 101 exist? NO, we no longer continue the sequence

        is 4 the start of a sequence? No, 3 exists (left neighbor), 

        200 is the start of a sequence. Yes it exists

        Does 1 start in the sequence? Yes, then we check for two
        '''


        numbers_set = set(nums)

        longest = 0

        for n in nums:
            # check if this is the start of a sequence
            if (n - 1) not in numbers_set:
                length = 0
                while (n + length) in numbers_set:
                    length += 1
                longest = max(length, longest)

        
        return longest
        
            