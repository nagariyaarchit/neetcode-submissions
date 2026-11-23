class Solution:
    def isPalindrome(self, s: str) -> bool:
        right = len(s) - 1
        left = 0
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif ((s[left].isalpha() and s[right].isalpha()) 
                and (s[left].lower() == s[right].lower())):
                left += 1
                right -= 1
                continue
            elif (s[left].isdigit() and s[right].isdigit() 
                and s[left] == s[right]):
                left += 1
                right -= 1
                continue
            else:
                return False
        return True
            




        