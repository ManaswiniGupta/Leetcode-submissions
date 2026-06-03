class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ss=[]
        tt=[]
        for i in s:
            if i!="#":
                ss.append(i)
            else:
                if ss:
                    ss.pop()
        for i in t:
            if i!="#":
                tt.append(i)
            else:
                if tt:
                    tt.pop()
        return ss==tt

        