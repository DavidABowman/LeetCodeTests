#Given the head of a singly linked list, return true if it is a palindrome or false otherwise

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.left = ListNode(0, head)
        if not head:
            return True

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            curr = slow
            slow = slow.next
            curr.next = prev
            prev = curr

        while prev:
            if prev.val != head.val:
                return False

            prev = prev.next
            head = head.next

        return True
'''
        def recursiveFunc(head):
            if not head:
                return True

            right = recursiveFunc(head.next)
            self.left = self.left.next
            return right and self.left.val == head.val
        return recrusiveFunc
'''