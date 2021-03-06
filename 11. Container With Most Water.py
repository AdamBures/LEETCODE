class Solution:
    def maxArea(self, height, result = 0, L = 0):
        if not height: return 0
        R = len(height)-1          
        while L != R:
            result = max(result, min(height[L], height[R])*(R-L))
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1                
        return result
