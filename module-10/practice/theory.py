from dataclasses import dataclass
from typing import Any, Optional
from collections import deque
from heapq import heappush, heappop

# # Односвязный список
# @dataclass
# class Node:
#     value: Any
#     next: Optional["Node"] = None

# c = Node("C")
# b = Node("B", next=c)
# a = Node("A", next=b)

# # A -> B -> C -> None
# print(a)
# print(a.next)
# print(b.next)


# def print_list(head: Optional[Node]) -> None:
#     current = head
#     while current is not None:
#         print(current.value, end=" -> ")
#         current = current.next
#     print("None")

# print_list(a)


# # Двусвязный список
# @dataclass
# class DoubleNode:
#     value: Any
#     next: Optional["DoubleNode"] = None
#     prev: Optional["DoubleNode"] = None

# a = DoubleNode("Page 1")
# b = DoubleNode("Page 2")
# c = DoubleNode("Page 3")

# a.next = b
# b.prev = a
# b.next = c
# c.prev = b

# print(c.prev.value)
# print(b.prev.value, "<->", b.value, "<->", b.next.value)


# stack = []
# stack.append("A")
# stack.append("B")
# stack.append("C")

# print("Стек:", stack)
# print("Последний элемент:", stack[-1])
# print(stack.pop())
# print("После pop:", stack)


# def is_balanced(text: str) -> bool:
#     stack = []
#     pairs = {")": "(",
#              "]": "[",
#              "}": "{"}
    
#     for char in text:
#         if char in "([{":
#             stack.append(char)
#         elif char in ")]}":
#             if not stack:
#                 return False
#             top = stack.pop()
#             if top != pairs[char]:
#                 return False
#     return len(stack) == 0
# print(is_balanced("(([]))"))
# print(is_balanced("(]"))
# print(is_balanced("][()]"))


# queue = deque()
# queue.append("A")
# queue.append("B")
# queue.append("C")

# print("Очередь:", queue)
# print("Выполнили:", queue.popleft())
# print("После выполнения:", queue)


# priority_queue = []
# heappush(priority_queue, (3, "C"))
# heappush(priority_queue, (1, "A"))
# heappush(priority_queue, (2, "B"))

# while priority_queue:
#     priority_n, task = heappop(priority_queue)
#     print(priority_n, task)


@dataclass
class TreeNode:
    value: Any
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None

root = TreeNode(
    "A",
    left = TreeNode(
        "B",
        left = TreeNode("D"),
        right = TreeNode("E") 
    ),
    right = TreeNode(
        "C",
        right = TreeNode("F")
    )
)

def preorder(node: Optional[TreeNode]) -> None:
    if node is None:
        return
    
    print(node.value)
    preorder(node.left)
    preorder(node.right)

print("Обход:")
preorder(root)