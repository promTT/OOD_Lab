class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return f"self.data = {self.data} self.next = {self.next.data}"


def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node


def insert_after_node(node, data):
    if node is None:
        print("Error: The given node is None")
        return

    new_node = Node(data)
    new_node.next = node.next
    node.next = new_node
    return node.next


def traverse(head):
    current = head
    while current.next:
        print(current.data, end=" <- ")
        current = current.next
    if current.data:
        print(current.data)
    else:
        print("None")
        
def find_next_node_data(head, find):
    current = head
    while current.next:
        if current.next.data == find:
            return current
        current = current.next
    return "not found"

print(" *** Locomotive ***")
inp = input("Enter Input : ").split()

head = Node(inp[0])

end = head
for i in inp[1:]:
    end = insert_after_node(end, i)
    
print("Before : ", end="")
traverse(head)

preHead = find_next_node_data(head, "0")
if preHead != "not found":
    newHead = preHead.next 
    preHead.next = None
    runner = newHead
    while runner.next != None:
        runner = runner.next
    runner.next = head
    head = newHead
print("After : ", end="")
traverse(head)