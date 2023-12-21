class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        map1={")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in map1.values() :
                stack.append(char)
                # print(char)
            else:
                if not stack:
                    # print(char,"false")
                    return False
                elif stack[-1]!= map1[char]:
                    return False

                else:
                     stack.pop()

        return not stack
                    
        