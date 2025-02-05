def linked_list_cycle(head):
    if not head:
        return None
    
    slow = fast = head
    while fast and fast.next: 
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False
    