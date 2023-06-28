
# to remove the duplicates from the linked list
def removeDuplicates(self, head):
        # code here
        # return head after editing list
        s = set()
        current = head
        if current == None:
            return head
        s.add(head.data)
        
        while( current != None and current.next != None ):
            if current.next.data in s:
                current.next = current.next.next
            else:
                s.add(current.next.data)
                current = current.next
        return head
            