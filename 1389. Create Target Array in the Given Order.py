from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        lst = []
        for num, indexes in zip(nums, index):
            lst.insert(indexes,num)

        return lst


if __name__ == "__main__":
    solution = Solution()
    solution.createTargetArray([0,1,2,3,4],[0,1,2,2,1])
