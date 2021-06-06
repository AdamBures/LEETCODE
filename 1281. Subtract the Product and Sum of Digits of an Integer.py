class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a = str(n)
        product = 1
        for i in range(len(a)):
            product *= int(a[i])

        total = 0  
        for i in range(len(a)):
            total += int(a[i])

        final = product - total
        return final
