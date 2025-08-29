#time complexity - o(n)
#space complexity - o(n)
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        lastSign = '+'

        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
               num = num*10 + int(c)
            if(not c.isdigit() and c != ' ') or (i == len(s) -1):
                if lastSign == '+':
                   stack.append(num)
                if lastSign == '-':
                   stack.append(-num)
                if lastSign == '*':
                   stack.append(stack.pop() * num)
                if lastSign == '/':
                   stack.append(int(stack.pop() / num))
                lastSign = c
                num = 0
        while len(stack) > 0:
            num = num + stack.pop()
        return num