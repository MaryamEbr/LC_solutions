# https://leetcode.com/problems/reverse-linked-list-ii/
# my solution works but it's not like what I saw in the LC solution, it seemed hard there! skip for now

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
    # wrong!
    def reverseBetween2(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        prev = None
        curr = head
        curr_pos = 1
        while curr:
            print("pos", curr_pos, " val: ", curr.val)
            if curr_pos < left:
                curr_pos += 1
                prev = curr
                curr = curr.next
            
            elif curr_pos > right:
                break
            
            else:
                curr_pos += 1
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
                
        return head
        
        
    # this just changes the values
    # I guess the time and space will be O(n), it works
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        
        rev_list = []
        curr = head
        curr_pos = 1
        while curr:
            if curr_pos < left:
                curr_pos += 1
                curr = curr.next
            
            elif curr_pos > right:
                break
            
            else:
                curr_pos += 1
                rev_list.append(curr.val)
                curr = curr.next

        rev_list = rev_list[::-1]        
        # print("rrrrev list ", rev_list)

        # second pass to change the values
        curr = head
        curr_pos = 1
        curr_rev_pos = 0
        while curr:
            # print("pos", curr_pos, " val: ", curr.val)
            if curr_pos < left:
                curr_pos += 1
                curr = curr.next
            
            elif curr_pos > right:
                break
            
            else:
                # print("******", curr_rev_pos, rev_list[curr_rev_pos])
                curr_pos += 1
                curr.val = rev_list[curr_rev_pos]
                curr_rev_pos += 1
                curr = curr.next   


        return head
    
sol = Solution()
ll = sol.reverseBetween(list_to_ll([1,2,3,4,5]), 2, 4)  
print_ll(ll)

