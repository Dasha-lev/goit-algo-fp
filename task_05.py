import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, node_colors):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node_colors[node[0]] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

#Нові функції для обходу в глибину та в ширину з кольорами
def dfs_with_colors(root):
    stack = [root]
    node_colors = {}
    color_step = 30  
    base_color = 0x111111

    while stack:
        node = stack.pop()
        hex_color = "#{:06x}".format(base_color)
        node_colors[node.id] = hex_color
        base_color += color_step  

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    draw_tree(root, node_colors)

def bfs_with_colors(root):
    queue = [root]
    node_colors = {}
    color_step = 30  
    base_color = 0x111111

    while queue:
        node = queue.pop(0)
        hex_color = "#{:06x}".format(base_color)
        node_colors[node.id] = hex_color
        base_color += color_step  

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    draw_tree(root, node_colors)


root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)


print("Обхід у глибину (DFS) з кольорами:")
dfs_with_colors(root)


print("Обхід у ширину (BFS) з кольорами:")
bfs_with_colors(root)
