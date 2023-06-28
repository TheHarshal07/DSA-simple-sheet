# Here we have to move the last element to the first of linked list
def Move_element(head):
    if (head.next == None):
        return head
    temp = head
    while(temp.next.next != None):
        temp = temp.next
    last = temp.next
    temp.next = None
    last.next = head
    return last 