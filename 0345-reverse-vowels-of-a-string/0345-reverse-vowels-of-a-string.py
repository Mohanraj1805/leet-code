class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = 'aeiouAEIOU'
        vowels_in_s = [i for i in s if i in vowel]  # Collect all vowels
        vowels_in_s.reverse()  # Reverse the vowels

        ans = ''
        vowel_index = 0

        for i in s:
            if i in vowel:
                ans += vowels_in_s[vowel_index]  # Replace with reversed vowel
                vowel_index += 1
            else:
                ans += i  # Keep the consonant as it is

        return ans

# Example usage:
# Create an instance of the Solution class and call the reverseVowels method
solution = Solution()
result = solution.reverseVowels("hello")
print(result)  # Output will be "holle"