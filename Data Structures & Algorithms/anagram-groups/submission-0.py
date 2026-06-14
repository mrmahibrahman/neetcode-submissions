class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = {(): []}
        
        
        # count = [0, 0 , 0...26]

        # note that list cannot be a key in a dictionary, must convert it to tuple

        # input = ["act","pots","tops","cat","stop","hat"]

        # the plan: 

        # the dictionary = key is the tuple that contains the letter frequencies for each word
        # value is the sublist that contains input word in the array that matches tuple

        # step 1: before we do the tuple, we will first use a list to get the frequencies of each character for each word

        # step 2: now that we got the frequencies, we will append the word to the value that maps to the key

        # return the values of the sublist as a list

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)
        
        return list(res.values())



