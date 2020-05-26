# Singly Linked List

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, data):
        # Create a new node using the value passed to the function
        newNode = Node(data)

        # if there is no head property, set the
        # head and the tail to be the newly created node
        if not self.head:
            self.head = newNode
            self.tail = self.head

        # Otherwise set the next property on the tail to be the
        # new node and set the tail property on the list
        # to be the newly created node
        else:
            self.tail.next = newNode
            self.tail = newNode

        # Increment length
        self.length += 1

        return SinglyLinkedList

    def pop(self):
        # If there are no nodes in the list, return undefined
        if not self.head:
            return None

        # Case if theres only 1 item in the array
        if self.head == self.tail:
            self.__init__()
            return None

        current = self.head

        # Loop through the entire list until you reach the tail
        while(current.next != self.tail):
            current = current.next

        # set the next property of the 2nd to last node to be null
        current.next = None
        self.tail = current

        # Decrement Length By One
        self.length -= 1

    def display_list(self):
        # Print List to Console
        current = self.head
        toString = "[ "
        while(current):
            toString += current.data + " "
            current = current.next

        print(toString + "]")

    def shift(self):
        if self.length == 0:
            return None

        current = self.head

        if not self.head.next:
            self.__init__()
            return current

        # Remove node from the beginning of the linked list
        self.head = current.next

        self.length -= 1

        return

    # Adding a new node to the beginning of the linked list
    def unshift(self, data):
        newNode = Node(data)

        # if there is no head property on the list, set the head
        # and tail to be the newly created node
        if not self.head:
            self.head = newNode
            self.tail = newNode
        # Otherwise set the newly created node's next
        # property to be the current head property on the list
        else:
            newNode.next = self.head
            # Set the head property on the list to be that newly created node
            self.head = newNode
        return SinglyLinkedList

    def get(self, index):
        if index > self.length or index < 0:
            return None

        current = self.head
        for i in range(index):
            current = current.next

        return current

    def set(self, index, value):
        getVal = self.get(index)
        if(getVal): getVal.data = value
        return getVal

newList = SinglyLinkedList()

newList.push("1")
newList.push("2")
newList.push("3")
newList.push("4")

newList.display_list()

newList.set(0, "100")

newList.display_list()

print ( newList.get(0).data )