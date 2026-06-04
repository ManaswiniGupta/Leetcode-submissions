class Solution:
    def pivotInteger(self, n: int) -> int:
        forward=[]
        backward=[]
        
        k=0 
        for i in range(1,n+1):
            k+=i
            forward.append(k)
        m=0
        for j in range(n,0,-1):
            m+=j
            backward.append(m)
        # print(forward, backward[::-1])
        # print(n)
        x=backward[::-1]
        
        for f in range(len(forward)):
            # print(forward[f], x[f])
            if forward[f] in x:
                # print(forward[f],x[f])
                if forward[f]==x[f]:
                    # print("he")
                    return f+1
            else:
                pass
        return -1


        