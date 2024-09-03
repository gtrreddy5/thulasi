class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Convert the string into the corresponding number based on the alphabet positions
        num_str = ''.join(str(ord(char) - ord('a') + 1) for char in s)
        
        # Perform the transformation k times
        for _ in range(k):
            num_str = str(sum(int(digit) for digit in num_str))
        
        # Return the final result as an integer
        return int(num_str)

# Example usage:
solution = Solution()
print(solution.getLucky("iiii", 1))  # Output: 36
print(solution.getLucky("leetcode", 2))  # Output: 6
print(solution.getLucky("gtr", 2))  # Output: 8
