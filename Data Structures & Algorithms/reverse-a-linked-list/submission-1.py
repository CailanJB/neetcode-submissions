# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Brute force solution: We can traverse the linked list and when we get to the end we traverse backwads adding each node to a seperate linked list changing their next pointers and keeping track of the next nodes: takes 0(N) space
        Optimal approach: we use 3 pointers:
        1. a pointer to the current node we are at
        2. A pointer to the next node
        3. A pointer to the previous node
        approach: we loop utnil our current node is null and at every node
        we switch the next pointer of the current node with the node prev is pointing to. before swapping we mus store the orignal next node of our current node so we dont lose the data.
        prev: will contain the new head of the linked list """
        #edge case empty list
        if not head:
            return None
        
        prev,curr = None,head

        while curr:
            #store the next node
            next_node = curr.next
            #swap curr.next with prev
            curr.next = prev
            #change prev to our current node
            prev = curr
            #change curr to next_node
            curr = next_node
        
        return prev
            