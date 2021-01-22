def reverseList(head):
    if not head or head.next == None: return head
    res = reverseList(head.next)
    head.next.next = head 
    head.next = None
    return res 
