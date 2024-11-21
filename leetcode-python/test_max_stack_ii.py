'''
https://leetcode.com/problems/max-stack/
'''

import collections
import heapq

# pylint: disable=C0116,C0103
class MaxStack:

    def __init__(self):
        self.stack = collections.deque()
        self.heap = []
        self.version = 0

    def push(self, x: int) -> None:
        self.version += 1
        # negative value for min-heap; version #; popped?
        # Later versions should get popped earlier from
        # a min-heap.
        l = [-x, -self.version, False]
        self.stack.append(l)
        heapq.heappush(self.heap, l)

    def pop(self) -> int:
        while self.stack[-1][2]:
            self.stack.pop()
        l = self.stack.pop()
        l[2] = True
        # print(f'Popped {result}; {len(self.stacks)} stacks')
        return -l[0]

    def top(self) -> int:
        while self.stack[-1][2]:
            self.stack.pop()
        # print(f'top(): {len(self.stacks)} stacks; returning {self.stacks[-1][-1]}')
        return -self.stack[-1][0]

    def peekMax(self) -> int:
        # print(f'peekMax(): {len(self.stacks)} stacks; returning {self.stacks[-1][0]}')
        while self.heap[0][2]:
            heapq.heappop(self.heap)
        return -self.heap[0][0]

    def popMax(self) -> int:
        while self.heap[0][2]:
            heapq.heappop(self.heap)
        l = heapq.heappop(self.heap)
        l[2] = True
        # If the maximum was the only element,
        # this stack will now be empty.
        # print(f'popMax() returned {result}: {len(self.stacks)} stacks')
        return -l[0]


stack = MaxStack()
stack.push(15)
stack.pop()
stack.push(1)
stack.push(-52)
stack.push(80)
stack.push(-39)
print(stack.popMax())
stack.push(91)
stack.pop()
stack.pop()
print(stack.top())
