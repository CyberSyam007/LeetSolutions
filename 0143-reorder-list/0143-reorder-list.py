# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp=head
        li=[]
        while temp:
            li.append(temp)
            temp=temp.next
        
        i=1
        j=len(li)-1
        temp=head
        for k in range(1,len(li)):
            if k%2==0 and j>=i:
                temp.next=li[i]
                temp=li[i]
                i+=1
            elif k%2!=0 and j>=i:
                temp.next=li[j]
                temp=li[j]
                j-=1
        temp.next=None
            

                    
        """
        Do not return anything, modify head in-place instead.
        """
        