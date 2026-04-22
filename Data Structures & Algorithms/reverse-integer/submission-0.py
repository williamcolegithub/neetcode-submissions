class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1   # 2147483647
        INT_MIN = -2**31      # -2147483648
        
        # Step 1: handle the sign
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Step 2: build the reversed number
        result = 0
        
        while x != 0:
            # pop the last digit off x
            digit = x % 10
            x =  x // 10
            
            # Step 3: overflow check BEFORE you multiply
            # (think: what would result * 10 + digit have to be bigger than to overflow?)
            if result > (INT_MAX - digit) // 10:
                return 0
            
            # push the digit onto result
            result = result *  10 + digit
        
        # Step 4: reapply the sign
        return result * sign