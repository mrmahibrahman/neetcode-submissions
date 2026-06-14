class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # one pointer starting index 0, another at index n - 1 (because array does not reach index n )  
        
        # if s[left pointer] == s[right pointer] then continue
        # if not equal then return false

        # if ends we return true
        # if left is <= the index on the right 

        lowercase_s = ""

        for c in s:
            if c.isalnum():
                lowercase_s += c.lower()
        i = 0
        j = len(lowercase_s) - 1 

        while i <= j:
            if lowercase_s[i] != lowercase_s[j]:
                return False

            i += 1
            j -= 1
        
        return True


