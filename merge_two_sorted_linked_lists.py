# https://leetcode.com/problems/merge-two-sorted-lists/

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
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        if list1==None:
            return list2
        
        if list2==None:
            return list1
        
        curr1 = list1
        curr2 = list2
        
        new_head = temp = ListNode(0)
        
        while curr1 != None and curr2 != None:
            print("curr1 ", curr1.val, " curr2 ", curr2.val)
            if curr1.val == curr2.val:
                temp.next = curr1
                curr1 = curr1.next
                
                temp = temp.next
                
                temp.next = curr2
                curr2 = curr2.next
                
                temp = temp.next
                
                
                
                
                
            elif curr1.val < curr2.val:
                temp.next = curr1
                curr1 = curr1.next
                
                temp = temp.next
                
                
                
            elif curr1.val > curr2.val:
                temp.next = curr2
                curr2 = curr2.next
                
                temp = temp.next
                
                
        while curr1:
            temp.next = curr1
            curr1 = curr1.next
            temp = temp.next
            
        
        while curr2:
            temp.next = curr2
            curr2 = curr2.next
            temp = temp.next
            
        return new_head.next        
        

sol = Solution()
# ll = sol.mergeTwoLists(list_to_ll([1,2,4]), list_to_ll([1,3,4]))  
ll = sol.mergeTwoLists(list_to_ll([1]), list_to_ll([2]))  
print_ll(ll)
        