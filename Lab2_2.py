class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            self._insert_at_end(data, self.head)

    def _insert_at_end(self, data, current_node):
        if not current_node.next:
            current_node.next = Node(data)
        else:
            self._insert_at_end(data, current_node.next)

    def insert_after_value(self, value1, value2):
        if not self.head:
            return
        else:
            self._insert_after_value(value1, value2, self.head)

    def _insert_after_value(self, value1, value2, current_node):
        if current_node.data == value1:
            new_node = Node(value2)
            new_node.next = current_node.next
            current_node.next = new_node
        elif current_node.next:
            self._insert_after_value(value1, value2, current_node.next)

    def print_list(self):
        if not self.head:
            print()
        else:
            self._print_list(self.head)

    def _print_list(self, current_node):
        print(current_node.data, end=' ')
        if current_node.next:
            self._print_list(current_node.next)
        else:
            print()

llist = LinkedList() #1
llist.insert_at_end(1) #2
llist.insert_at_end(2) #4
llist.insert_at_end(3) #5
llist.insert_at_end(4) #7
llist.insert_at_end(5) #8
llist.print_list()

llist.insert_after_value(1, 10) #3
llist.insert_after_value(3, 20) #6
llist.insert_after_value(5, 30) #9

llist.print_list()
