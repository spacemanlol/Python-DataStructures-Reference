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

    # Remove node from the beginning of the linked list
    def display_list(self):
        # Print List to Console
        current = self.head
        toString = "[ "
        while(current):
            toString += current.data + " "
            current = current.next

        print(toString + "]")

    # Remove node from the beginning of the linked list
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

    # Get value at specific index within linked list
    def get(self, index):
        if index > self.length or index < 0:
            return None

        current = self.head
        for i in range(index):
            current = current.next

        return current

    # Set Value at specific index within the linked list
    def set(self, index, value):
        getVal = self.get(index)
        if(getVal): getVal.data = value
        return getVal

    # Adding a node to the linked list at a specific position
    def insert(self, index, data):

        # if the index less than zero or greater than the length, return false
        if index < 0 or index > self.length:
            return False

        # if the index is the same as the length, push a new node to the end of the list
        if index == self.length:
            self.push(data)
            return True

        # if the index is 0, unshift a new node to the start of the list
        if index == 0:
            self.unshift(data)
            return True

        # Create new node
        newNode = Node(data)

        # Otherwise, using the get method, access the node at the [index - 1]
        getValue = self.get(index - 1)

        # Set the next property on that node to be the new node
        next = getValue.next
        getValue.next = newNode

        # Set the property on the new node to be the previous next
        newNode.next = next

        # Increment Length
        self.length += 1

        return True

    # Removing a node from the Linked List at a specific index
    def remove(self, index):
        # Value to be removed
        toRemove = None

        # If the index is less than zero or greater than the length, return undefined
        if index < 0 or index >= self.length:
            return toRemove

        # If the index is the same as the length-1, pop
        if index == self.length - 1:
            toRemove = self.pop()
        # If the index is 0, use shift
        elif index == 0:
            toRemove = self.shift()
        else:
            # Otherwise, using the get method, access the node at index - 1
            getValue = self.get(index - 1)

            # Value to be removed
            toRemove = getValue.next

            # Set the next property on that node to be the next of the next node
            getValue.next = getValue.next.next

        self.length -= 1
        return toRemove



newList = SinglyLinkedList()

newList.push("1")
newList.push("2")
newList.push("3")
newList.push("4")

newList.display_list()


newList.remove(3)
newList.display_list()
