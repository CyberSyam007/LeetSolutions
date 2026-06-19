# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter=0
        temp=head
        while temp:
            temp=temp.next
            counter+=1
        if counter>1:
            target=counter-n+1
            if target!=1:
                cur=head
                prev=None
                x=1
                while cur and x!=target:
                    prev=cur
                    cur=cur.next
                    x+=1
                prev.next=cur.next
                cur.next=None
                return head
            elif target==1:
                head=head.next
                return head 
        else:
            return None