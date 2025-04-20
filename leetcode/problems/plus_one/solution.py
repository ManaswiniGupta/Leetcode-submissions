class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        sum=1
        for i in range(len(digits)):
            sum+=digits[i]*(10**(len(digits)-1-i))
        l=[int(i) for i in str(sum)]
        return l

        # n=len(digits)
        
        # while n>0:
        #     a=sum//(10**(n-1))
        #     sum=sum-a*10**(n-1)
           

            
           
        #     l.append(a)
        #     n-=1
        

        # return l
            
           
        