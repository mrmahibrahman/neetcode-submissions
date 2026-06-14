class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If they are not even the same length, we already know 
        # this is not an anagram
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        # Iterate through the length of string s, both s and t are the same length anyways
        for i in range(len(s)): 
            # countS[s[i]] = 1 + countS[s[i]] // this is going to throw a key error, what if the character does not exist in the hash map?
            countS[s[i]] = 1 + countS.get(s[i], 0) # the second param is if this key does not exist in the hash map, the default value is 0
            countT[t[i]] = 1 + countT.get(t[i], 0) 

        for c in countS:
            # we use get because what if the character (key) in countS[c] is not in countT? we add a default value in countT
            if countS[c] != countT.get(c,0):
                return False

        return True


        