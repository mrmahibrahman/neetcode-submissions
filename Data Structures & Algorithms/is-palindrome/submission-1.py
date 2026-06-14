class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # one pointer starting index 0, another at index n - 1 (because array does not reach index n )  
        
        # if s[left pointer] == s[right pointer] then continue
        # if not equal then return false

        # if ends we return true
        # if left is <= the index on the right 

        lowercase_s = ""
        characters = ['0','1','2','3','4','5','6','7','8','9','a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        for c in s:
            c = c.lower()
            if c in characters:
                lowercase_s += c
        i = 0
        j = len(lowercase_s) - 1 

        print(lowercase_s)   

        while i <= j:
            if lowercase_s[i] != lowercase_s[j]:
                return False

            i += 1
            j -= 1
        
        return True


