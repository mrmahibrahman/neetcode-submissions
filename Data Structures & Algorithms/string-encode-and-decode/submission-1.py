class Solution:

    '''
    To encode a list of strings to just one string

    decode = decode that one string into a list of strings

    strs == strs2 

    encode steps: 
    1. traverse through the input and we can just add elements together since 
    you can add strings
    2. you could get the length of each string and store it in a hashmap (key: word, value: length of the string)

    decode steps: 
    1. use the hashmap and just  

    
    We can assume that we have any possible character in the input 
    
    how do we create some kind delimiter when one word ends and when one word begins

    ["neet", "code"]

    we can encode to a string by putting a pound sign between the two words
    "neet#code", but this approach might not work because the delimiter might 
    show up in some of the words like "neet", "co#de". this is an issue for decoding





    '''

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res


    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) # how many following characters we have to read after j 
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        
        return res
