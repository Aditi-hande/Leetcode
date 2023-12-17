class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        current_score = 0

        for char in s:
            if char == '(':
                stack.append(current_score)
                current_score = 0
            else:
                current_score = stack.pop() + max(2 * current_score, 1)

        return current_score