class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n != 1:
            if n%2 == 0:
                n //= 2
                matches += n
                print(n)
            else:
                n = (n - 1) // 2 + 1
                matches += n
                print(n)
        matches -= 1
        return matches

if __name__ == "__main__":
    solution = Solution()
    solution.numberOfMatches(7)
