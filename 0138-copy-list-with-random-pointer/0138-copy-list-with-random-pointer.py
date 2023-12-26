"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        cur=head

        while cur: #interweaved the linkedlist
            new= Node(cur.val)
            new.next=cur.next
            cur.next=new
            cur=new.next
        
        #assign random ptrs to new nodes

        cur=head

        while cur:
            cur.next.random=cur.random.next if cur.random else None
            cur=cur.next.next
        
        #remove connections

        old_head=head
        new_head=head.next
        ocur=old_head
        ncur=new_head

        while ocur:
            ocur.next=ncur.next
            ncur.next=ncur.next.next if ncur.next else None
            ocur=ocur.next
            ncur=ncur.next

        return new_head
        


        
        