from typing import List
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        cur_max = 0
        cur_answ = None
        choices_ctx = {}
        for e in A:
            cur_choice_ctx = choices_ctx.get(e,0) + 1
            choices_ctx[e] = cur_choice_ctx
            if cur_choice_ctx > cur_max:
                cur_max = cur_choice_ctx
                cur_answ = e
        return cur_answ


print (Solution().repeatedNTimes([1,2,3,3]))