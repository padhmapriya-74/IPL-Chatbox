from collections import deque

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def bfs_search(root, target_name):
    if root is None:
        return None

    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        if node.name == target_name:
            return node

        for child in node.children:
            queue.append(child)

    return None

# Create the tree
matches = Node("matches")
csk = Node("csk")
rcb = Node("rcb")
lsg = Node("lsg")
kkr = Node("kkr")
mi = Node("mi")
gt = Node("gt")
dc = Node("dc")
pbks = Node("pbks")
rr = Node("rr")
srh = Node("srh")

matches.add_child(csk)
matches.add_child(rcb)
csk.add_child(lsg)
csk.add_child(kkr)
rcb.add_child(mi)
rcb.add_child(gt)
lsg.add_child(dc)
kkr.add_child(pbks)
mi.add_child(rr)
gt.add_child(srh)

# Get input for the node to be searched
target_node = input("Enter the node to search: ")

# Perform BFS search and return the node if found
result = bfs_search(matches, target_node)

if result:
    print(result.name)
else:
    print("Node not found.")
