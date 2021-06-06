class Solution:
    def maximum69Number (self, num: int) -> int:
        maximum = num
        s = [x for x in str(num)]
        six_flag = None
        for i in range(len(s)):
            if s[i] == "6":
                s[i] = str(9)
                six_flag = True
            else:
                s[i] = str(6)
                six_flag = False
            temp = int("".join(s))
            maximum = max(maximum,temp)
            if six_flag:
                s[i]=str(6)
            else:
                s[i]=str(9)
            
        return maximum
