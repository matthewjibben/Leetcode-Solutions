# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution A: (iterative)
#   loop through the list once, reversing each connection
#   afterwards, the last element is the head
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current = head
        while(current != None):
            # print(current.val)
            n = current.next
            current.next = prev
            prev = current
            current = n

        return prev

# Solution B: (recursive)
# 
# class Solution(object):
#     def reverseList(self, head, prev=None):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """        
#         if(head == None):
#             return prev
#         else:
#             n = head.next
#             head.next = prev
#             return self.reverseList(n, head)



if __name__ == '__main__':
    s = Solution()

    head3 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5)))))
    test = s.reverseList(head3)

    print("solution =")
    h = test
    while(h != None):
        print(h.val)
        h = h.next

