class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
       
        # First step: create a hashmap that counts the frequencies
        # Key: the number, value = the frequency that number appears
        count = {} # O(1)

        # second step: we are also going to create buckets where the index of the array
        # is equal to the frequency, and inside that index contains a bucket (array) that
        # contains all the numbers that map to that frequency
        # freq = [[] for i in range(len(nums) + 1)]
        freq = [] # O(1)
        for i in range(len(nums) + 1): # (O(n + 1))
            freq.append([]) # O(1)

        # third step: loop through the nums list, we will count the frequencies each number appears
        for num in nums: # O(n)
            count[num] = 1 + count.get(num, 0) # O(1)

        # fourth step: loop through the counts hashmap, we will map the frequencies (the index) and put the 
        # corresponding number into the bucket
        # [            []    [1,2]     []       ]
        # Frequencies: 0     1       2
        # O()
        for num, cnt in count.items(): # O(n)
            freq[cnt].append(num)

        # fifth step: We will create an empty result list
        res = []

        # sixth step: we are going to loop through the buckets starting from teh highest frequency to the lowest
        # we are going to check each of the numbers inside the bucket and append it to the results list
        for i in range(len(freq) - 1, 0, -1): #
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return res



        # sevent step: If the results list length is equal to k, we know we found our k most frequent elements and return that! 


        # okay so notes: 
        # we need len(nums) + 1 for buckets because worse case we could have this: 
        # [5,5,5,5,5] where the frequency of 5 is 5

        # so when we initialize our list
        # we need to do for i in range(len(nums) + 1) which will create SIX slots (0,1,2,3,4,5) instead of (0,1,2,3,4)