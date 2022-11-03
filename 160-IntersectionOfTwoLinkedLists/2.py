# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA = headA
        stackA = []
        currB = headB
        stackB = []
        while currA != None:
            stackA.append(currA)
            currA = currA.next

        while currB != None:
            stackB.append(currB)
            currB = currB.next

        if stackA[-1] != stackB[-1]:
            return None

        while stackA[-1] == stackB[-1]:
            intersection = stackA[-1]
            stackA.pop()
            stackB.pop()
            if len(stackB) == 0 or len(stackA) == 0:
                break

        return intersection
