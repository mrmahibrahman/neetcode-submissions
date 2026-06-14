class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Steps: 
        # 1: Go through each item in the nums array
        # 2: If the number is not in the hash set, add it to the hash set
        # 3: If the number is in the hashset, we have our duplicate

        hashset = set()

        # Step 1: 
        for num in nums:
            # Step 2 and 3
            if num in hashset:
                return True
            else: 
                hashset.add(num)
        
        return False

            
        