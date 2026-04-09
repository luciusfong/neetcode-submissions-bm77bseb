class Solution:
    def isValid(self, s: str) -> bool:
        matching = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for c in s:
            if c in matching:
                stack.append(c)
            else:
                if not stack or matching[stack[-1]] != c:
                    return False
                stack.pop()
        return len(stack) == 0