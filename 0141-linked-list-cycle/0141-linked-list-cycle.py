# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d={}
        flag=0
        counter=0
        temp=head
        while temp:
            if temp not in d:
                d[temp]=counter
                counter+=1
                temp=temp.next

            elif temp in d:
                return True

        return False
            

        
        