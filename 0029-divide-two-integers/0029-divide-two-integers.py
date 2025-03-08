class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Edge case: If dividend is equal to divisor
        if dividend == divisor:
            return 1
        
        # Handle the sign using XOR logic
        sign = (dividend < 0) == (divisor < 0)
        int_max = 2**31 - 1
        int_min = -2**31
        
        # Take the absolute value
        n, d = abs(dividend), abs(divisor)
        ans = 0
        
        # Bitwise shifting to speed up the division
        while n >= d:
            count = 0
            # Shift divisor to left until it's just less than dividend
            while n >= (d << count):
                count += 1
            # Decrement count by 1 (because last shift was invalid)
            count -= 1
            
            # Add the power of two to the answer
            ans += 1 << count
            # Subtract the large chunk from dividend
            n -= d << count
        
        # Apply sign to the result
        ans = ans if sign else -ans
        
        # Handle integer overflow
        if ans >= int_max:
            return int_max
        if ans <= int_min:
            return int_min
        
        return ans
