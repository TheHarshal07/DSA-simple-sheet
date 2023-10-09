# TO count the number of nodes in link list

class Node:
    # Function to initialize the Node object
    def __init__(self, item):
        self.item = item
        self.next = None
    
class Linklist:
    # Function to initialize the head
    def __init__(self):
        self.head = None

    # Logic to count the number of link list
    def CountLinklist(self):
        current = self.head
        count=0

        while(current):
            count += 1
            current = current.next
        return count

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.item, end=" ")
            temp = temp.next

if __name__ == '__main__':

    link_list = Linklist()

    link_list.push(20)
    link_list.push(30)
    link_list.push(40)
    link_list.push(50)

    print("The given link list is :")
    link_list.printlist()

    link_list.CountLinklist()
    print("\n The count of the link list is :")
    link_list.CountLinklist()