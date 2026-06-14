class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        # step 1: 
        s_hashmap = {}
        t_hashmap = {}

        # step 2: 
        for i in range(len(s)):
            if s[i] in s_hashmap:
                s_hashmap[s[i]] = s_hashmap.get(s[i]) + 1
            else: 
                s_hashmap[s[i]] = 1
            
            if t[i] in t_hashmap:
                t_hashmap[t[i]] = t_hashmap.get(t[i]) + 1
            else: 
                t_hashmap[t[i]] = 1

        # step 3: compare hashmaps 
        if s_hashmap == t_hashmap:
            return True
        else: 
            return False
            



        