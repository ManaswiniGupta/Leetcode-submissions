class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        tot=0
        for i in range(num1, num2+1):
            if i<100:
                tot+=0
            else:
                k=str(i)
                for j in range(1,len(k)-1):
                    if int(k[j-1])<int(k[j])>int(k[j+1]):
                        tot+=1
                    elif int(k[j-1])>int(k[j])<int(k[j+1]):
                        tot+=1
        return tot


        