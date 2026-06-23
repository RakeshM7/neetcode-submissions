class Solution:

    def encode(self, strs: List[str]) -> str:
        char_counts = []
        for value in strs:
            char_counts.append(len(value))
        encoded_str = ""
        for i in range(0, len(char_counts)):
            encoded_str += f"{char_counts[i]}#{strs[i]}"
        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        source_list = []
        ptr = 0
        while ptr < len(s):
            char_count = 0
            while s[ptr] != '#':
                char_count = char_count*10 + int(s[ptr])
                ptr += 1
            source_list.append(s[ptr+1:ptr+1+char_count])
            ptr = ptr + 1 + char_count
        return source_list

           
            
            
            
            
            
            
            

