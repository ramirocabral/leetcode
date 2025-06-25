class Solution :
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in "([{":
                stack.append(c)
            elif c in ")]}":
                if len(stack) > 0:
                    aux = stack.pop()
                else:
                    return False
                if not self.isValidClosingChar(c, aux):
                    return False
        
        if not len(stack) == 0:
            return False

        return True
        
    
    def isValidClosingChar(self, c, aux : str) -> bool:
        if c == ")":
            return (aux == "(")
        elif c == "}":
            return (aux == "{")
        elif c == "]":
            return (aux == "[")
            
        return False
