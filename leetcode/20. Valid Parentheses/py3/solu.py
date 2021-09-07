#0328
class Solution:
    def isValid(self, s: str) -> bool:
        thestack = []
        leftbra = ['[', '{', '(']
#        themap = {']': '[', '}': '{', ')': '(' }
        themap = {'[': ']', '{': '}', '(': ')' }
        for it in s:
            if it in leftbra:
#                thestack.insert(it, 0)
                thestack.append(it)
#                print('stack: ', thestack)
            else:
                if 0 == len(thestack):
                    return False
                tail = thestack.pop()
#                print('tail: ', tail)
                expecting = themap[tail]
#                print('expecting: ', expecting)
                if expecting == it:
                    continue
                else:
                    return False
        if 0 == len(thestack):
            return True
        else: 
            return False

                


