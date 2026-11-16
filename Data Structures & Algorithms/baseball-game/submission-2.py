class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """Approach we need to keep track of the previous elements we saw and when we make a new record we also need o keep track. Henmce we shall use a stack to keep track of the elements we are going to. We add numbers to the stack. and when we hit a operation we add the vales the values from the stack and perform operation adding the values back to the stack along with the new value. We don need to pop the values to perfrom the operation only if the operation is C"""
        stack = []
        #go through the operations adding numbers to the stack
        #when we envounter an operation pop from the stack
        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "C":
                stack.pop()
            else:
                #this is a number so we add it to the stakc
                stack.append(int(op))
        
        return sum(stack)
        

          




        