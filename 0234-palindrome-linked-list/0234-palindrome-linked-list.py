# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # to optimize O(1) space, reverse second half of list and then compare
        #can find mid using fast slow pointer
        
        fast=slow=head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        #slow will be at mid
        
        #reverse from mid to end
        prev=None
        cur=slow
        while(cur):
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        
        #compare
        
        lo=head
        hi=prev
        
        while hi:
            if lo.val!=hi.val:
                return False
            lo=lo.next
            hi=hi.next
        return True
        
        
            
        

        
        
        
#         end=head
#         s="".join(str(end.val))
#         while end.next:
#             end=end.next
#             s=s+str(end.val)

            
#         return s==s[::-1]
#since space is O(n)