# 234. Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solutions:
# Solution A: O(n) time, O(n) space
#   loop through the linked list and add each value to a new list
#   afterwards, have use two pointers to check if each value is equal, iterating until they meet at the center
# Solution B:
#   Initialize a fast and slow pointer, where slow iterates 1 node at a time, and fast iterates 2 at a time
#   When fast hits the end of the list, then slow is at the midpoint.
#   Now, reverse the direction of the nodes in the second half, so that all nodes point inward (towards the center node)
#   Example: 1 -> 2 -> 3 <- 2 <- 1
#   Example 2 (even length): 1 -> 2 -> 2 <- 1 (the slow pointer will stop when it reaches the "dead end" node that everything will point towards)
#   loop through the list from the start and end to the center. If the values are ever different, return False

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # when fast hits the end of the list, then slow is at the midpoint
        fast = head
        slow = head

        while(fast != None):
            fast = fast.next
            if(fast != None):
                fast = fast.next
            else:
                break
            slow = slow.next
        
        # reverse the direction of the nodes in the second half, so that all nodes point inward
        # the slow pointer will be at the "dead end" node that everything will point towards
        prev = slow
        slow = slow.next
        prev.next = None
        while(slow != None):
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        
        # loop through the list from the start and end to the center. If the values are ever different, return False
        fast = head
        slow = prev
        while(slow != None):
            if(fast.val != slow.val):
                return False
            slow = slow.next
            fast = fast.next
        
        return True



if __name__ == '__main__':
    head = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=2, next=ListNode(val=1))))
    s = Solution()
    test = s.isPalindrome(head)
    print("solution =", test)

    head2 = ListNode(val=1, next=ListNode(val=2))
    test = s.isPalindrome(head2)
    print("solution =", test)

    head3 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=2, next=ListNode(val=1)))))
    test = s.isPalindrome(head3)
    print("solution =", test)