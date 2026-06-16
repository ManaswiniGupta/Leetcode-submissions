class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        prev = 0

        for pos in spaces:
            res.append(s[prev:pos])
            res.append(" ")
            prev = pos

        res.append(s[prev:])

        return "".join(res)
