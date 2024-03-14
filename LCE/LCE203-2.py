#Given the head of a linked list and an integer val, 
#remove all the nodes of the linked list that has Node.val == val, 
#and return the new head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #Handle the case where the head is None
        while head is not None and head.val == val:
            head = head.next
        current = head
        #Iterate through the node and remove nodes with specified values
        while current is not None and current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return head
'''
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = head
        
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        
        return head.next if head and head.val == val else head
'''