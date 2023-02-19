# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    # wrong, not working with the edge cases
    def isValid1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        latest_open = ""
        for c in s:
            print("^" , stack, "latest ", latest_open)
            if c in ["[", "{", "("]:
                print(" in ")
                stack.append(c)
                latest_open = c
                
            elif c == "]" and len(stack)>0:
                print (" out] ")
                poped = stack.pop()
                if poped != "[" or latest_open != "[":
                    return False
            elif c == "}"and len(stack)>0:
                print(" out} ")
                poped = stack.pop()
                if poped != "{" or latest_open != "{":
                    return False
            elif c == ")" and len(stack)>0:
                print(" out) ")
                poped = stack.pop()
                if poped != "(" or latest_open != "(":
                    return False
        
        if len(stack)>0:
            return False
        return True
    
    
    def isValid(self, s):
        
        open_list = ["(", "{", "["]
        close_list = [")", "}", "]"]
        stack = []
        latest_in = ""
        
        for c in s:
            print(" - ", c, " stack ", stack, " latest ", latest_in)
            if c in open_list:
                
                stack.append(c)
                latest_in = c
                
            elif c in close_list:
                if len(stack)==0:
                    return False
                else:
                    popped = stack.pop()
                    print("*******", open_list.index(latest_in))
                    if close_list[open_list.index(popped)] != c:
                        return False
                    
        if len(stack)>0:
            return False
        return True
              
        
sol = Solution()
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))
print(sol.isValid("]"))
print(sol.isValid("["))

