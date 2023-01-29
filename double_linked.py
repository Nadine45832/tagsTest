class Node:
    def __init__(self, value=None, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous

def get_node_by_index(head, index):
    node = head
    while index:
        node = node.next
        index -= 1
    return node

def return_last_element(head):
    node = head
    while node.next:
        node = node.next
    return node

def insert_element(head, value, index=None):
    new_node = Node(value)
    if index == 0:
        next_node = head
        head.previous = new_node
        new_node.next = head
        return new_node        
    previous_node = get_node_by_index(head, index - 1) if index else return_last_element(head)
    next_node = previous_node.next
    previous_node.next = new_node
    new_node.previous = previous_node
    if next_node:
        next_node.previous = new_node
        new_node.next = next_node
    return head

def detete_element(head, index):
    node = get_node_by_index(head, index)
    next_node = node.next if node else None
    previous_node = node.previous if node else None
    if previous_node:
        previous_node.next = next_node
    if next_node:
        next_node.previous = previous_node
    return head if previous_node else next_node

def print_list(head):
    node = head
    node_list = []
    while node:
        node_list.append(node.value)
        node = node.next
    print(node_list)

head = Node(2)

head = insert_element(head, 4)
head = insert_element(head, 7)
head = insert_element(head, 9)
head = insert_element(head, 12)
head = insert_element(head, 19)
head = insert_element(head, 23, 0)

#head = detete_element(head, 3)

print_list(head)


class Queue():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def pop(self):
        if self.size == 0:
            raise IndexError('Queue is empty')
        node = self.head
        self.head = node.next
        self.head.previous = None
        self.size -= 1
        return node.value

    def push(self, value):
        node = Node(value)
        if self.size != 0:
            node.previous = self.tail
            self.tail.next = node
        self.tail = node
        if self.size == 0:
            self.head = node
        self.size += 1

    def size(self):
        return self.size

    def print(self):
        node = self.head
        node_list = []
        while node:
            node_list.append(node.value)
            node = node.next
        print(node_list)

queue_1 = Queue()
queue_1.push(12)
queue_1.push(22)
queue_1.push(14)
queue_1.push(15)
queue_1.push(178)
queue_1.push(100)
queue_1.print()
int_1 = queue_1.pop()
queue_1.push(99)
int_2 = queue_1.pop()
queue_1.push(55)
queue_1.push(88)
queue_1.print()
