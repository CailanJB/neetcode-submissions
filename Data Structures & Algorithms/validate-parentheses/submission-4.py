class Solution:
    def isValid(self, s: str) -> bool:
        """Edge case if we envounter a clsoed brakcet and the stakc is empty we immediately return false because that means we never encountered a open braxcket to match the clsoed brakcet."""
        if s == '[]':
            return True
        
        stack = []
        for char in s:
            if char in {'(','{','['}:
                stack.append(char)
            else:
                #ensure the stack isnt empty
                if stack:
                    bracket = stack.pop()
                    if char == ')' and bracket != '(':
                        #then this is not balanced
                        return False
                    elif char == '}' and bracket != '{':
                        #then this is not balanced
                        return False
                    elif char == ']' and bracket != '[':
                        #then this is not balanced
                        return False
                else:
                    return False
        
        return True if not stack else False


        