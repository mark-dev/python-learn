class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jset = set(J)
        ctx = 0
        for s in S:
            if s in jset:
                ctx += 1     
        return ctx