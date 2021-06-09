class LinkedList:
    # Create list with empty 'head' node
    def __init__(self):
        self.head = None


class Node:
    # Each node has a value and a reference to next node
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def addFirst(e, L):
    # New head, with old head as it's next value
    L.head = Node(e, L.head)


def addLast(e, L):
    # Iterate through the linked list until there is no 'next' node.
    if L.head:
        current_node = L.head
        while 1:
            if current_node.next is None:
                # Append new node
                current_node.next = Node(e)
                break
            current_node = current_node.next
    else:
        L.head = Node(e)


def removeFirst(L):
    # New head is the old heads 'next' node.
    if L.head:
        L.head = L.head.next


def removeLast(L):
    if L.head:
        # Iterate through linked list until there is no 'next' node.
        current_node = L.head
        while 1:
            # Keep track of previously explored node
            prev_node = current_node

            if current_node.next is None:
                # Remove last node by removing previous nodes 'next' reference
                prev_node.next = None
                break
            current_node = current_node.next


def getFirst(L):
    if L.head:
        # Return integer value of last node
        return L.head.value
    else:
        # If nothing in list, return None.
        return None


def getLast(L):
    if L.head:
        current_node = L.head
        # Iterate through the list until at linked list's last node
        while 1:
            if current_node.next is None:
                # Returns integer value of last node
                return current_node.value
            current_node = current_node.next
    else:
        # If nothing in list, return None.
        return None


def showList(L):
    # List of node objects to be printed
    to_print = []
    if L.head:
        current_node = L.head
        to_print.append(current_node)
        # Iterate through linked list, appending each node to to_print list.
        while current_node.next is not None:
            to_print.append(current_node.next)
            current_node = current_node.next
    # Print linked list node values with "->" between each.
    string = " -> ".join(str(x.value) for x in to_print)
    # Print the linked list if it contains any elements
    if string:
        print(string)
