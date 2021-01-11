class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()

        dict = {'(': ')',
                '{': '}',
                '[': ']'}

        if len(s) % 2 == 1:
            return False

        for i in s:
            if i in dict:
                if not stack or stack[-1] != dict[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)

        return not stack

