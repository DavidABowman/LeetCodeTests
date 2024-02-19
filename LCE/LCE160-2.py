#Given the heads of two singly linked-lists headA and headB, 
#return the node at which the two lists intersect. 
#If the two linked lists have no intersection at all, return null.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #1) Find lengths of both lists
        lenA, lenB = 0, 0
        currA, currB = headA, headB
        while currA:
            lenA += 1
            currA = currA.next
        while currB:
            lenB += 1
            currB = currB.next
        #2) Reset Pointers
        currA, currB = headA, headB
        #3) Move pointer of longer list to starting point
        if lenA > lenB:
            for _ in range(lenA - lenB):
                currA = currA.next
        else:
            for _ in range(lenB - lenA):
                currB = currB.next
        #4) Move both pointers simultaneously until they meet
        while currA !=  currB:
            currA = currA.next
            currB = currB.next
        #5) Returns intersection node or none if no intersection
        return currA
'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        stackA = ['A']
        stackB = ['B']

        while headA or headB:
            if headA:
                stackA.append(headA)
                headA = headA.next

            if headB:
                stackB.append(headB)
                headB = headB.next

        prev = None
        while stackA and stackB:
            nodeA = stackA.pop(-1)
            nodeB = stackB.pop(-1)

            if nodeA != nodeB:
                return prev

            prev = nodeA
'''