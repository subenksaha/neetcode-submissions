class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for st in strs:
            l = len(st)
            encoded_str += f"#{l}${st}"

        return encoded_str

    def decode(self, s: str) -> List[str]:
        curr = None
        l = len(s)
        i = 0
        f = 0
        e = 0
        decoded = list()
        while i < l:
            if s[i] == "#": f = i
            if s[i] == "$": e = i
            
            if f < e and (e-f) > 0:
                print(f,e)
                cls = s[f+1:e]
                cl = int(cls)
                cp = s[e+1 : e+1+cl]
                decoded.append(cp)
                f = 0
                e = 0
            i += 1
            
        return decoded