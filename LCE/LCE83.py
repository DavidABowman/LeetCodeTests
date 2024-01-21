#Given the head of a sorted linked list,
#delete all duplicates such that each element appears only once.
#Return the linked list sorted as well.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n=head
        if head is None:
            return None
        while n is not None and n.next is not None:
            #print(n.val)
            if n.val==n.next.val:
                n.next=n.next.next
            else:
                n=n.next
        return head

'''
#I dont know how a LinkedList works - I do at the very least know how it works though
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        __init__(self, data)
            insertAtBegin(i)
                if insertAtBegin(i) == insertAtIndex(i+1):
                    remove_node(i+1)
                else:
                    printLL()

'''