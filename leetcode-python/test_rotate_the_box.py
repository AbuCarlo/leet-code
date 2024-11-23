'''
https://leetcode.com/problems/rotating-the-box
'''

from typing import List


# pylint: disable=C0103
def rotateTheBox(box: List[List[str]]) -> List[List[str]]:
    for l in box:
        obstacle = len(l)
        for i in range(len(l) - 1, -1, -1):
            c = l[i]
            if c == '*':
                obstacle = i
            elif c == '#':
                # This stone comes to rest on the
                # previous obstacle, and becomes a new one.
                # The current cell is left empty.
                obstacle -= 1
                l[i], l[obstacle] = '.', '#'
            else:
                assert l[i] == '.'
        
        # Now rotate the whole thing Pythonically.
        # Tip of the hat to https://stackoverflow.com/a/8421412/476942
        # This gives us tuples...
        return list(zip(*reversed(box)))



sample = [["#",".","#"]]

print(rotateTheBox(sample))
