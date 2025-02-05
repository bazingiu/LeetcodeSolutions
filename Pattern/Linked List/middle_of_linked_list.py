class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = next 
        
def middle_of_linked_list(head):
    if not head:
        return None
    slow = fast = head
    while fast and fast.next: 
        fast = fast.next.next
        slow = slow.next
    return slow
    