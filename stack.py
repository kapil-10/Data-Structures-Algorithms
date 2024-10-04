from collections import deque

class stack:
    def __init__ (self):
        self.stacks = deque()

    def push (self,value):
        self.stacks.append(value)
        return self.stacks

    def pop(self):
        return print(self.stacks.pop())
        
    
    def peek(self):
        for key,value in enumerate(self.stacks):
            print('At index ',key,'The value is ',value)

    def is_empty(self):
        if len(self.stacks) == 0:
             print('the length of stack is zero(0)')
        else:
            print('the length of stack is not zero(0)')

            
    def size(self):
        return print('The size of the stack is' ,len(self.stacks) )
    
    def clear(self):
        return self.stacks.clear()
    
# Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial.
# reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"   

def rev_string(s):
    stack_object = stack()

    for char in s:
        stack_object.push(char)

    print(stack_object)

    rev_s =[]
    while stack_object != 0:
        rev_s.append(stack_object.pop())

    print(rev_s)

 # Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.
    # is_balanced("({a+b})")     --> True
    # is_balanced("))((a+b}{")   --> False
    # is_balanced("((a+b))")     --> True
    # is_balanced("))")          --> False
    # is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True
    


def check_paranthesis(input_symbols):
    possible_parrantheses ={'{':'}' , '(':')' , '[':']'}
    stack_string = stack()
    stack_string.clear()
    for s_val in  input_symbols:
        if s_val in possible_parrantheses.keys(): 
                stack_string.push(s_val)
                print('The string appended to stack is ',s_val)

    for s_val in possible_parrantheses.values():
            stack_string.pop()
            print('The string pop is ',s_val)

    print ('The stack is currently',stack_string.peek())

    if stack_string is None:
         return 'balanced string'
    else:
         return'not balanced string'


    



if __name__ == '__main__':
    s = stack()

    arr = range(1,5)

    for value in arr:
        s.push(value)
        

    s.peek()

    s.is_empty()

    s.size()

    for to_remove_val in range(1,5):
        s.pop()
    

    s.size()

    string = 'ver'
    rev_string(string)
    s.clear()
    
    y={'{':'}' , '(':')' , '[':']'}
    check_paranthesis(y)