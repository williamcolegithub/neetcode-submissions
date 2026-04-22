class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n  # (1) what initial value makes sense?
        
        # First pass: fill output[i] with product of everything LEFT of i
        left = 1 # (2) starting value for a running product
        for i in range(n):  # (3) which direction do we iterate?
            output[i] = left  # (4) what goes here BEFORE updating left?
            left *= nums[i]  # (5) what operator updates the running product?
        
        # Second pass: multiply in product of everything RIGHT of i
        right = 1  # (6) starting value for the right-side running product
        for i in range(n-1, -1, -1):  # (7) bounds + step for reverse iteration
            output[i] *= right  # (8) how do we combine with existing value?
            right *= nums[i]  # (9) same pattern as before
        
        return output