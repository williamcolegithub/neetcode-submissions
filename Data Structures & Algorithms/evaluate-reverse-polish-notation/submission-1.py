class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                left, right = stack.pop(), stack.pop()
                stack.append(right-left)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                left,right = stack.pop(), stack.pop()
                stack.append(int(right / left))
            else:
                stack.append(int(c))

        return stack[0]
