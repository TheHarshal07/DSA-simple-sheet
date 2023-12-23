'''
Here we want to convert Binary linked list to an integer
for e.g

linked list = 1 -> 0 -> 1
so 101 -> 5 in binary representation

'''
class Node:
    def __init__(self,item) -> None:
        self.item = item
        self.next = None

class Linkedlist:
    def __init__(self) -> None:
        self.head = None
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def BinaryConversion(self):
        res = 0
        curr = self.head
        while(curr != None):
            res= res<<1
            res += curr
            self.head = self.head.next
        return res
    
    def printLinkedlist(self):
        temp = self.head
        while(temp):
            print(temp.item, end="")
            temp = temp.next

if __name__ == '__main__':
    link_list = Linkedlist()

    link_list.push(1)
    link_list.push(0)
    link_list.push(1)

    link_list.printLinkedlist()
    print("Binary conversion of the linked list:")

    link_list.BinaryConversion()
