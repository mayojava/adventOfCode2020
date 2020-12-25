def main():
    f = open('day18.txt', 'r')

    sm = 0

    for line in f:
        line = line.strip()

        stack = []

        for i in range(0, len(line)):
            current = line[i].strip()
            if len(current) == 0: continue
            
            if current == '(' or is_sign(current):
                stack.append(current)
            elif current.isdigit():
                stack.append(current)
            elif current == ')':
                expr = []
                while stack[-1] != '(':
                    expr = [str(stack.pop(-1))] + expr
                stack.pop(-1)
                stack.append(solver(expr))
            
        res = solver(stack)
        #print(res)
        sm += res
    
    print(sm)

def eveluate(expr):
    if len(expr) == 1:
        return int(expr[0])

    res = int(expr[0])
    for i in range(1, len(expr)):
        if is_sign(expr[i]):
            res = calculate(res, expr[i], expr[i+1])
    return res

def solver(items):
    stack = []
    
    for i in items:
        if type(i) == int or i.isdigit():
            if len(stack) == 0:
                stack.append(int(i))
            else:
                if stack[-1] == '+':
                    stack.pop(-1)
                    sm = stack.pop(-1) + int(i)
                    stack.append(sm)
                else:
                    stack.append(int(i))
        else:
            stack.append(i)
    
    res = 1
    for val in stack:
        if val != '*':
            res *= val
    return res


        

def is_sign(ch):
    return ch == '+' or ch == '*'

def calculate(op1, opr, op2):
    if opr == '+':
        return int(op1) + int(op2)
    else:
        return int(op1) * int(op2)

if __name__ == '__main__':
    main()