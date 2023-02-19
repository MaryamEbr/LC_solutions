#https://leetcode.com/problems/middle-of-the-linked-list/




def list_to_ll(l):
    current = dummy_head = ListNode(0)
    for val in l:
        current.next = ListNode(val)
        current = current.next
    
    return dummy_head.next


def print_ll(ll):
    while ll:
        print("^", ll.val)
        ll = ll.next
        
        
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
            
        # first pass to get the length of linked list
        ll_length = 0
        curr = head
        while curr:
            ll_length += 1
            curr = curr.next
                
        # second pass to get the middle node
        pos = 0
        curr = head
        while curr:
            if pos == int(ll_length/2):

                return curr
            pos += 1
            curr = curr.next

sol = Solution()
new_ll = sol.middleNode(list_to_ll([1,2,3,4,5,6]))
print_ll(new_ll)