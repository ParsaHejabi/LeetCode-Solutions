# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hash_table = {}

        currA = headA
        hash_table[currA] = True
        while currA.next != None:
            hash_table[currA.next] = True
            currA = currA.next

        currB = headB
        if currB in hash_table.keys():
            return currB

        while currB.next != None:
            if currB.next in hash_table.keys():
                return currB.next
            currB = currB.next

        return None
