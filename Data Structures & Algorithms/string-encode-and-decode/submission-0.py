class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for st in strs:
            l = len(st)
            encoded_str += f"{l}${st}"

        return encoded_str

    def decode(self, s: str) -> List[str]:
        curr = None
        l = len(s)
        i = 0
        decoded = list()
        while i < l:
            if s[i] == "$":
                cls = s[:i]
                cl = int(cls)
                cp = s[i+1 : i+cl+1]
                s = s[cl+2:]
                decoded.append(cp)
                i = 0
                l -= cl+2
            i += 1
            
        return decoded