class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



def removeElements(self, head: ListNode, val: int): -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while head is not None:
        if head.val == val:
            prev.next = head.next
        else:
            prev = prev.next 
        head = head.next

    return dummy.next
    


