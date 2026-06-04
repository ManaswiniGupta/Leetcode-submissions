class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        answer=[0]*len(temperatures)
        
        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                    remove_ele = stack.pop()
                    answer[remove_ele]=i-remove_ele
            stack.append(i)
        return answer




        # return answer



        