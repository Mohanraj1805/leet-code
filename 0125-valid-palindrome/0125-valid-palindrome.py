class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Remove non-alphanumeric characters and convert to lowercase
        filtered_str = ''.join(char.lower() for char in s if char.isalnum())
        
        # Check if the filtered string is a palindrome
        return filtered_str == filtered_str[::-1]
