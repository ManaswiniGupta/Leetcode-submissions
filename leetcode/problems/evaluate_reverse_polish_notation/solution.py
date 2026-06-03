class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i.lstrip("-").isdigit():
                stack.append(int(i))
            elif i=="+":
                a=stack[-1]+stack[-2]
                stack.pop()
                stack.pop()
                stack.append(a)
            elif i=="-":
                b=stack[-2]-stack[-1]
                stack.pop()
                stack.pop()
                stack.append(b)
            elif i=="*":
                c=stack[-1]*stack[-2]
                stack.pop()
                stack.pop()
                stack.append(c)
            elif i=="/":
                d=int(stack[-2]/stack[-1])
                stack.pop()
                stack.pop()
                stack.append(d)
        return stack[0]
            

        