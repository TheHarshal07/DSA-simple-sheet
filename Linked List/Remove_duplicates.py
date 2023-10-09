# TO remove the duplicates from the link list 

class Node:
    # Creating Node
    def __init__(self,item):
          self.item = item
          self.next = None

class Linklist:
     # maintaining the head
     def __init__(self):
          self.head = None


     # This is logic to remove the duplicates node from the given link list
     def RemoveDuplicates(self):
          temp = self.head
          s = set()
          if (temp == None):
               return self.head
          s.add(self.head)

          while(temp != None and temp.next != None):
               if temp.next.item in s:
                    temp.next = temp.next.next
               else:
                    s.add(temp.next.item)
                    temp = temp.next
          return self.head
     
     # Inserted the nodes
     def push(self, new_data):
          new_node = Node(new_data)
          new_node.next = self.head
          self.head = new_node

     # To print all the nodes
     def printlist(self):
          temmp = self.head
          while(temmp):
               print(temmp.item, end=" ")
               temmp = temmp.next

                
if __name__ == '__main__':
     
     link_list = Linklist()

     link_list.push(10)
     link_list.push(12)
     link_list.push(12)
     link_list.push(13)

     print("The given link list is :")
     link_list.printlist()

     link_list.RemoveDuplicates()

     print("\nThe updated link list is :")
     link_list.printlist()

    




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
            