from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        count = 0        
        for word in words:
            for letter in word:
                if letter not in allowed:
                    count += 1
                    break
        
        return len(words) - count

if __name__ == "__main__":
    solution = Solution()
    solution.countConsistentStrings("abc", ["a","b","c","ab","ac","bc","abc"])
