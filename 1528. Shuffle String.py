from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = list(zip(s,indices))
        message = ""
        sorted_result = sorted(result, key=lambda t: t[1])
        for letter_tuple in sorted_result:
            message += letter_tuple[0]
        return message

if __name__ == "__main__":
    solution = Solution()
    solution.restoreString("codeleet", [4,5,6,7,0,2,1,3])
