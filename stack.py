class Stack(object):
     
     # Initializes the stack
     def __init__(self):
         self.stack = []
         
     # Check is the stack is empty. Needed for pop() 
     def isEmpty(self):
         return self.stack == []
         
     # Push
     def push(self, intNumber):
        #only add a value if it is an integer
        if isinstance( intNumber, int ):
         self.stack.append(intNumber)
        else:
           print("Not an integer!")

     # Pop
     def pop(self):
         # Only pop a value if the stack is not empty
         if(self.isEmpty()):
           print("Is empty!") 
         else:         
           return self.stack.pop()

     # Check the size of the stack
     def checksize(self):
         return len(self.stack)
         


