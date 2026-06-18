# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        elif not list1 and list2:
            return list2
        elif list1 and not list2:
            return list1

        i=list1
        j=list2
        if list1.val < list2.val:
            temp=list1
            i=i.next
        else:
            
            temp=list2
            j=j.next
        head=temp
        while i and j :
            if i.val < j.val:
                temp.next=i
                temp=i
                i=i.next
            else:
                temp.next=j
                temp=j
                j=j.next
        if not i and j:
            temp.next=j
        elif i and not j:
            temp.next=i
        return head