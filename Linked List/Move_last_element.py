# To Move the last element to the first of link list

class Node:
    # Created Node
    def __init__(self, item):
        self.item = item
        self.next = None

class Linklist:
    # Create link list

    def __init__(self):
        self.head = None
    
    # Logic for moving the nodes from last to first position
    def Move_lastEle(self):
        temp = self.head
        if (temp == None):
            return temp
        while(temp.next.next != None):
            temp = temp.next
        last = temp.next
        temp.next = None
        last.next = self.head
        self.head = last
        

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.item,end="")
            temp = temp.next


if __name__ == '__main__':
    link_list = Linklist()

    link_list.push(1)
    link_list.push(2)
    link_list.push(3)

    print("The given link list :")
    link_list.printlist()

    link_list.Move_lastEle()

    print("\nThe updated link list is :")
    link_list.printlist()


        



# Here we have to move the last element to the first of linked list
# def Move_element(head):
#     if (head.next == None):
#         return head
#     temp = head
#     while(temp.next.next != None):
#         temp = temp.next
#     last = temp.next
#     temp.next = None
#     last.next = head
#     return last 