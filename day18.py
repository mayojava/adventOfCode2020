def main():
    f = open('day18.txt', 'r')

    sm = 0

    for line in f:
        line = line.strip()

        stack = []

        for i in range(0, len(line)):
            current = line[i].strip()
            if len(current) == 0: continue
            
            if current == '(':
                stack.append('(')
            elif is_sign(current):
                stack.append(current)
            elif current.isdigit():
                if len(stack) == 0:
                    stack.append(current)
                elif is_sign(stack[-1]):
                    expr = [current]
                    while len(stack) > 0 and stack[-1] != '(' and stack[-1] != ')':
                        expr = [stack.pop(-1)] + expr
                    stack.append(eveluate(expr))
                else: stack.append(current)
            elif current == ')':
                expr = []
                while stack[-1] != '(':
                    expr = [str(stack.pop(-1))] + expr
                stack.pop(-1)
                stack.append(eveluate(expr))
            
            #print(stack)


        if len(stack) == 1:
            #print('res', stack[0])
            sm += stack[0]
        else:
            res = int(stack[0])
            for k in range(1, len(stack)):
                if is_sign(stack[k]):
                    res = calculate(res, stack[k], stack[k+1])
            sm += res   
            #print('res', res)
    
    print(sm)

def eveluate(expr):
    if len(expr) == 1:
        return int(expr[0])

    res = int(expr[0])
    for i in range(1, len(expr)):
        if is_sign(expr[i]):
            res = calculate(res, expr[i], expr[i+1])
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