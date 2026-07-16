class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in range(len(tokens)):
            print(i,stk)
            if tokens[i] in "+-*/":
                num2 = int(stk.pop())
                num1 = int(stk.pop())
                match tokens[i]:
                    case "+":
                        stk.append(str(num1+num2))
                    case "-":
                        stk.append(str(num1-num2))
                    case "*":
                        stk.append(str(num1*num2))
                    case "/":
                        stk.append(str(int(num1/num2)))
            else:   
                stk.append(tokens[i])
        return int(stk.pop())