#bb3323 Bavanan Bramillan and william wranovsky wbw32

from stackclass import Stack

###
"""
the postfix function uses postfix notation and the stack class to make tokens using expression and push/pop for each operand
"""
###

def postfix(exp):
    stack = Stack()
    tokens = exp.split()
    
    for token in tokens:
        if token.isdigit() or (token[1:].isdigit() and token[0] == '-'): #checks for token for numbers or negative numbers
            stack.push(float(token)) #adds token to stack as a float
        else:
            #pops in backwards to get from top
            operand2 = stack.pop() 
            operand1 = stack.pop()

            if token == '+':  #token is +, add
                result = operand1 + operand2
                stack.push(result)
            elif token == '*':  #token is *, mult
                result = operand1 * operand2
                stack.push(result)
            elif token == '/':  #token is /, div
                result = operand1 / operand2
                stack.push(result)
            elif token == '-':  #token is -, sub
                result = operand1 - operand2
                stack.push(result)
    

    return stack.pop()

if __name__ == "__main__":
    print("Welcome to Postfix Calculator")
    print("Enter exit to quit")
    
    while True:
        exp = input("Enter Expression (put a space after each one): ")
        if exp == "exit":
            print("Exiting...")
            break
        result = postfix(exp)
        print("Result:", result)

