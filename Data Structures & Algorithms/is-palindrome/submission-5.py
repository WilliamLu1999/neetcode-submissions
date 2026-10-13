class Solution:
    def isPalindrome(self, s: str) -> bool:
        sn = "".join(char for char in s if char.isalnum())
       
        sn = sn.lower()
        print(sn)
        i = 0
        j = len(sn)-1

        while i < j and len(sn)>0:
            if sn[i]!=sn[j]:
                # print(s[i],s[j])
                return False
            else:
                i+=1
                j-=1
        return True
