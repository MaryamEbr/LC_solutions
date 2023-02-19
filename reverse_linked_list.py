# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# inversing the ll while traversing
# time is O(n) and space is O(1)
def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    
    prev = None
    curr = head
    while curr:
        next_one = curr.next
        curr.next = prev
        prev = curr
        curr = next_one

    head = prev
    return head
        
        
        

    


ll_list = [1 , 2, 3, 4, 5]
current = dummy_head = ListNode(-100)
for val in ll_list:
    current.next = ListNode(val)
    current = current.next
    
the_ll = dummy_head.next

rev_ll = reverseList(the_ll)

#### print the linked list
the_ll_temp = rev_ll
while the_ll_temp:
    print("^", the_ll_temp.val)
    the_ll_temp = the_ll_temp.next
