'''
https://leetcode.com/problems/max-stack/
'''

import collections
import heapq

class MaxStack:

    def __init__(self):
        self.stack = collections.deque()
        self.heap = []
        self.pop_counts = collections.Counter()

    def push(self, x: int) -> None:
        self.stack.append(x)
        heapq.heappush(self.heap, -x)

    def pop(self) -> int:
        result = self.stack.pop()
        if result == -self.heap[0]:
            heapq.heappop(self.heap)
        # print(f'Popped {result}; {len(self.stacks)} stacks')
        return result
        
    def top(self) -> int:
        # print(f'top(): {len(self.stacks)} stacks; returning {self.stacks[-1][-1]}')
        return self.stack[-1]

    def peekMax(self) -> int:
        # print(f'peekMax(): {len(self.stacks)} stacks; returning {self.stacks[-1][0]}')
        return self.heap[0]

    def popMax(self) -> int:
        result = -heapq.heappop(self.heap)
        if result == self.stack[-1]:
            self.stack.pop())
        else:
            self.pop_counts[result] += 1
        # If the maximum was the only element,
        # this stack will now be empty.
        # print(f'popMax() returned {result}: {len(self.stacks)} stacks')
        return result


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()