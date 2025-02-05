class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_by_value(head, val):
    dummy = ListNode(0)  # Dummy node to handle edge cases
    dummy.next = head
    prev, curr = dummy, head

    while curr:
        if curr.val == val:
            prev.next = curr.next  # Bypass the current node
        else:
            prev = curr
        curr = curr.next

    return dummy.next  # Return new head (skipping dummy)
