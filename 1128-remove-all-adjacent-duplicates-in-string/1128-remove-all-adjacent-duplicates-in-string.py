class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        top = -1
        for i in s:
            if stack and stack[top] == i:
                stack.pop()
                top -= 1
            else:
                stack.append(i)
                top += 1
        return "".join(stack)