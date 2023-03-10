# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None, val_list=None):
        self.val = val
        self.next = next
        if val_list:
            self.val = val_list[0]
            if val_list[1:] != []:
                self.next = ListNode(val_list=val_list[1:])
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sumlist = ListNode()
        current = sumlist
        leading1 = 0
        while l1 or l2 or leading1:
            value = leading1
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
            leading1 = 0
            if value > 9:
                leading1 = 1
                value %= 10
            
            current.val = value
            
            if l1 or l2 or leading1:
                current.next = ListNode()
                current = current.next

        

        return sumlist






if __name__ == '__main__':
    l1 = ListNode(val_list=[9,9,9,9,9,9,9])
    l2 = ListNode(val_list=[9,9,9,9])

    s = Solution()
    slist = s.addTwoNumbers(l1, l2)
    
    current = slist
    while current:
        print(current.val)
        current = current.next

