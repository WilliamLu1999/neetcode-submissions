class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_lst = list(s)
        t_lst = list(t)
        s_lst.sort()
        t_lst.sort()
        return s_lst==t_lst