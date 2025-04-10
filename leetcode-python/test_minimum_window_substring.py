'''
https://leetcode.com/problems/minimum-window-substring/

"Given two strings s and t of lengths m and n respectively, return the minimum 
window substring of s such that every character in t (including duplicates) is
included in the window. If there is no such substring, return the empty string.

'''

class ZeroingCounter(collections.Counter):
    '''
    This class encapsulates the logic of a sliding count. If any count
    becomes 0, the key is deleted.
    '''

    # We don't need to override the constructor since the initial
    # values will not include 0s. update() should be overriden, but
    # we never invoke it.

    def __setitem__(self, key, value):
        if value == 0:
            self.pop(key)
        else:
            super().__setitem__(key, value)

def minimum_window_substring(s: str, t: str) -> str:
    allowable = set(t)
    counts = ZeroingCounter(t)
    overflow = ZeroingCounter()
    result = None
    r = 0
    for r, c in enumerate(s):
        if c not in allowable:
            continue
        if c in counts:
            counts[c] -= 1
            if len(counts) == 0:
                print(f"Found match from {l} to {r}")
        else:
            overflow[c] += 1


    return result