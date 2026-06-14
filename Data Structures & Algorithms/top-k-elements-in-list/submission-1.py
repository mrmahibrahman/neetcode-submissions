class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        res = []

        # first
        for i in range(len(nums)):
            counter[nums[i]] += 1
          
        for i in range(k): 
            mostFrequent = max(counter, key=counter.get)
            counter.pop(mostFrequent)
            res.append(mostFrequent)
            # so here this is O(N*k) because max is an O(N) operation
        
        return res



        # time complexity is O(n*k)
       
        # # nums = [1,2,2,3,3,3], return the k most frequent elements

        # # hashmap 
        # # key = the number 
        # # and value is = frequency of the number that appears

        # # first: you would use a for loop to iterate through the nums array
        #     # DURING each iteration: 
        #     ''' 
        #     you would add the element as the key and then update the count by one
        #     '''
        #     # O(n)
        
        # # # now we have our final hashmap
        # # {1: 1, 
        # # 2: 2, 
        # # 3: 3}

        # # so now we have to output our top two elements
        # # mostFrequent = max(hashmap) # worst case is probably O(1)
        # # hashmap.pop(mostFrequent) (o(1))


        # # array.append(mostFrequent) (o(1))
        # # mostFrequent = max(hashmap) (o(1) to O(n)
        # # print(the list)







        