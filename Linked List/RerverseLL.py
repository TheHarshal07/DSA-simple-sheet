# # Creating link list

class Node:
    # Creating Node
    def __init__(self,item):
        self.item = item
        self.next = None
class LinkedList():   
    # Creating link list
    def __init__(self):
        self.head = None
    
    # login to reverse the link list
    def reverse(self):
        prev = None
        curr = self.head
        while(curr != None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printlinklist(self):
        temp = self.head
        while(temp):
            print(temp.item, end=" ")
            temp = temp.next

if __name__ == '__main__':

    link_list = LinkedList()

    link_list.push(3)
    link_list.push(2)
    link_list.push(1)

    print("The given list :")
    link_list.printlinklist()
    link_list.reverse()
    print("\nThe reverse link list :")
    link_list.printlinklist()

# here we want to create a link list

# class Node:
#     def __init__(self, item) -> None:
#         self.item = item
#         self.next = None
    
# class Linklist():
#     def __init__(self) -> None:
#         self.head = None

    
#     def push(self, new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node

#     def reverse(self):
#         prev = None
#         curr = self.head
#         while(curr != None):
#             next = curr.next
#             curr.next = prev
#             prev = curr
#             curr = next
#         self.head = prev

#     def printLinklist(self):
#         temp = self.head
#         while(temp):
#             print(temp.item, end=" ")
#             temp = temp.next
        
# if __name__ == "__main__":
#     link_list = Linklist()

#     link_list.push(3)
#     link_list.push(2)
#     link_list.push(1)

#     link_list.printLinklist()
#     link_list.reverse()
#     print("\n")
#     link_list.printLinklist()

