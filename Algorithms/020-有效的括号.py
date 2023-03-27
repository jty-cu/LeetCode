## 栈，左括号入栈，右括号去和最近的左括号进行匹配

class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        if len(s)%2 == 1:
            return False
        left = []
        for c in s:
            if c in ['(', '[', '{']:
                left.append(c)
            else: ## 右括号
                if left and d[c] == left[-1]:
                    left.pop()
                else:
                    return False
        return not left