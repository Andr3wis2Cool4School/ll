def partition(head, x):
    p = less = ListNode(0)
    q = more = ListNode(0)

    while head != None:
        if head.val < x:
            less.next = head
            less = less.next
        else:
            more.next = head
            more = more.next
        head = head.next 

    more.next = None
    less.next = q.next
    return p.next
    
