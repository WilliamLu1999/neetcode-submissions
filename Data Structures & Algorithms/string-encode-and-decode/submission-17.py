class Solution:

    def encode(self, strs: List[str]) -> str:
        temp_str = ""
        for s in strs:
            temp_str += str(len(s))
            temp_str += '#'
            temp_str += s
            

        # print(temp_str)
        return temp_str
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j= i            
            while s[j]!='#':
                j+=1
            length =int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j+1+length
        return res