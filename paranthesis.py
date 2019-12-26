class Solution:
    def isValid(self, s: str) -> bool:
        opening = ['[', '(', '{']
        closing = [']', ')', '}']
        pairs = [('[', ']'), ('(', ')'), ('{', '}')]
        lenght = len(s)
        stack = []
        counter = 0
        if s == None:
            return True
        for i in s:
            if i in opening:
                counter += 1
                stack.append(i)

            elif i in closing:
                counter -= 1
                if counter < 0 or counter > lenght / 2:
                    return False
                ele = stack.pop()

                if (ele, i) not in pairs:
                    return False

        if len(stack) > 0:
            return False
        else:
            return True