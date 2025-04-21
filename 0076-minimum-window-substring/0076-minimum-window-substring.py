
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Step 1: Initialize the needed variables
        if not s or not t:
            return ""
        
        # Frequency of characters in t
        dict_t = Counter(t)
        
        # Number of unique characters we need to match in the window
        required = len(dict_t)

        # Left and Right pointers of the sliding window
        l, r = 0, 0
        
        # To track how many characters in the window match the required ones in t
        formed = 0
        
        # This will store the character counts in the current window
        window_counts = {}

        # The answer tuple will hold: (window_length, left, right)
        ans = float("inf"), None, None

        # Step 2: Start sliding window with the right pointer
        while r < len(s):
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1
            
            # If character is part of t and we have met its required frequency, increase 'formed'
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Step 3: Try to shrink the window while we have a valid window
            while l <= r and formed == required:
                character = s[l]
                
                # Update the answer if the current window is smaller
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                # Shrink the window from the left
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                
                l += 1    

            # Move the right pointer forward
            r += 1

        # Step 4: Return the result
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]
