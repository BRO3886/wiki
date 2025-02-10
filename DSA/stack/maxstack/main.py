class Node:
    def __init__(self, key):
        self.key = key
        self.next: Node = None
        self.prev: Node = None


"""
DLL to act like a stack
deletion will be O(1) when I know the node

priority queue -> to get the max element -> store the node

sorted dict -> 
key = element value
val = [list of nodes]

push:
1. create node
2. point the stack top to this node
3. point prev of this node to stack top
4. move top pointer to this node
5. push the key to sorted dict

pop:
point top to node->prev

peekMax:
sorted dict can help

popMax:
get max key from sorted dict
get node at last index in value list of dict
delete the node from the value list, delete node from DLL
"""
from sortedcontainers import SortedDict


class MaxStack:
    def __init__(self):
        self.head: Node = Node(float("-inf"))
        self.last: Node = None
        self.sd = SortedDict()

    def push(self, item):
        n = Node(item)

        if self.last is None:
            self.head.next = n
            n.prev = self.head
        else:
            self.last.next = n
            n.prev = self.last

        self.last = n
        if self.sd.get(item) is None:
            self.sd[item] = [n]
        else:
            self.sd[item].append(n)

    def pop(self):
        if self.last is None:
            raise IndexError("stack is empty")

        temp = self.last
        if temp.prev == self.head:
            self.last = None
            raise IndexError("stack is empty")

        self.last = temp.prev
        self.last.next = None

        l = self.sd.get(temp.key)[:-1]
        self.sd[temp.key] = l
        if len(l) == 0:
            self.sd.pop(temp.key)

        return temp.key

    def peekMax(self):
        k, _ = self.sd.peekitem()
        return k

    def popMax(self):
        k, v = self.sd.peekitem()
        last = v[-1]
        v = v[:-1]
        if len(v) == 0:
            del self.sd[k]
        else:
            self.sd[k] = v

        pred = last.prev
        suc = last.next
        pred.next = suc
        if suc is not None:
            suc.prev = pred

        if last.next is None:
            temp = self.last
            self.last = temp.prev

        return last.key

    def top(self):
        if self.last is None:
            raise IndexError("stack is empty")
        return self.last.key

    def print(self):
        temp = self.head
        temp = temp.next
        arr = []
        while temp:
            arr.append(temp.key)
            temp = temp.next

        print(*arr)
        print(self.sd.keys())


if __name__ == "__main__":
    s = MaxStack()
    s.push(5)
    # s.print()
    s.push(1)
    # s.print()
    s.push(5)
    # s.print()
    print("top", s.top())
    # s.print()
    print("popMax", s.popMax())
    # s.print()
    print("top", s.top())
    # s.print()
    print("peekMax", s.peekMax())
    # s.print()
    print("pop", s.pop())
    # s.print()
    print("top", s.top())
    # s.print()
