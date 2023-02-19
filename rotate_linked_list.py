# https://leetcode.com/problems/rotate-list/


def list_to_ll(l):
    current = dummy_head = ListNode(0)
    for val in l:
        current.next = ListNode(val)
        current = current.next
    
    return dummy_head.next


def print_ll(ll):
    while ll:
        print("^^", ll.val)
        ll = ll.next
        

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        

        new_head = head # to be change
        curr = head
        temp_list = []
        
        # traverse to locate the new head O(n)
        while curr:
            temp_list.append(curr.val)
            curr = curr.next
        
        if len(temp_list)==0:
            return head
        
        new_head_pos = len(temp_list) - k%len(temp_list)
        
        # edge cases
        if new_head_pos<0 or new_head_pos==len(temp_list) or new_head_pos==0:
            return head
        
        # traverse to set the new head
        # setting the pre new head nore to None next
        curr = head
        prev = None
        pos = 0
        while curr:
            if pos == new_head_pos:
                new_head = curr
                prev.next = None

            prev = curr
            curr = curr.next
            pos += 1
        
        #currently prev is pointing at the last node
        # the curr.next to prev head
        prev.next = head
        
        return new_head
        

sol = Solution()
new_ll = sol.rotateRight(list_to_ll([1,2,3,4,5]), 11)
# new_ll = sol.rotateRight(list_to_ll([17,75,80,87,44,45,75,86,74,20]), 19)
print_ll(new_ll)