#Given the head of a singly linked list, reverse the list, and return the reversed list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#Val = Value, Next points to Next Node
#Dinal Node points to none - showing its end
#Singly linked list - no moving backwards, only forwards
'''
Create blank node, traverse list, each time popping last node and appending it to list
-This runs in O(N^2) :(

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list = None # None is always Final element in any linked list
        current = head #head of List taken as argument, current builds and traveses list

        while current: #True if CUrrent =! None
            next_node = current.next #Points Next Var to Next Node to 
            current.next = new_list #End at new list
            new_list = current#Always pointing to new head of reverse list
            current = next_node #Now we're repeating and looping, to reverse list
            #We're using 2 var to advance list, 
            #whilst new_list keeps track of head of reversed list
            #Finished when Current  = None, meaning loop finishes
        
        return new_list
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        current_node = head
        while current_node:
            next_node = current_node.next #Store next code
            current_node.next = prev_node #Reverse the pointer
            #Move pointers in one direction
            prev_node = current_node
            current_node = next_node
        return prev_node