def remove_duplicates(head):
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next  # Remove duplicate
        else:
            curr = curr.next
    return head
