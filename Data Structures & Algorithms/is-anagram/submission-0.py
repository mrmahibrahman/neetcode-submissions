class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: transform the two strings into dictionaries 
        # the key is the character from the string,
        # the value is the frequency of each letter in the string

        # Step 2: Then you go through the dictionaries and see if the frequency of each letter
        # is the same for input string s and input string t

        # Step 1
        letter_frequency_1 = {}
        letter_frequency_2 = {}

        for char in s:
            if char not in letter_frequency_1:
                letter_frequency_1[char] = 1
            else: 
                letter_frequency_1[char] += 1

        for char in t:
            frequency = letter_frequency_2.get(char)

            if frequency is None:
                letter_frequency_2[char] = 1
            else:
                letter_frequency_2[char] += 1
        

        # Step 2
        for key, frequency_1 in letter_frequency_1.items():
            frequency_2 = letter_frequency_2.get(key)
            
            if frequency_1 != frequency_2:
                return False
            else:
                continue
        
        for key, frequency_2 in letter_frequency_2.items():
            frequency_1 = letter_frequency_1.get(key)

            if frequency_2 != frequency_1: 
                return False
            else:
                continue
        
        return True
        







        

