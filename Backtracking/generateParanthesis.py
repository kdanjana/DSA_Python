""" 
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""


def generateParenthesis(n: int):
    path = []
    res = []
    def backtrack(open_count, close_count):
        if open_count == close_count == n:
            res.append("".join(path))
            return
        if open_count > n or close_count > n or open_count < close_count:
            return
        if open_count < n:
            path.append("(")
            backtrack(open_count+1, close_count)
            path.pop()
        if close_count < open_count:
            path.append(")")
            backtrack(open_count, close_count+1)
            path.pop()
    backtrack(0,0)
    return res


print(generateParenthesis(3))