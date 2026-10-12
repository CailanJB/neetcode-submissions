class MinStack:
    """In order for consatnt time oeprations for get_min we need ot keep trakc of the smallest avlue on the stakc by sugn an additonal stack calle dmin stack. the second stack will always keep the smallets value at the top of the stack. when pushing values we take the min between the value we want to insert and the cyrrent smallest and add to the stack. When popping when popping we pop from both stacks. ex: if we add 1,2,3,2,0 min stack would have 1,1,1,1,0"""

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        if self.min_stack:
            min_val = min(val,self.min_stack[-1])
            self.min_stack.append(min_val)
            self.stack.append(val)
        else:
            self.min_stack.append(val)
            self.stack.append(val)
        
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
