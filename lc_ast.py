import ast
import graphviz

class AstToDot(ast.NodeVisitor):
    def __init__(self):
        self.dot = graphviz.Digraph(comment='AST', graph_attr={'rankdir': 'TB'})
        self.node_counter = 0
        self.node_map = {} # Maps AST node objects to their unique ID in Graphviz

    def get_new_node_id(self, node):
        node_id = f"node_{self.node_counter}"
        self.node_counter += 1
        self.node_map[node] = node_id
        return node_id

    def visit(self, node):
        node_id = self.get_new_node_id(node)

        # Determine label for the node
        label = type(node).__name__
        if hasattr(node, 'name'): # For ClassDef, FunctionDef, Name
            label += f"\nName: {node.name}"
        elif hasattr(node, 'id'): # For Name (when it's an identifier)
            label += f"\nID: {node.id}"
        elif hasattr(node, 'value'): # For Constant (e.g., numbers, strings)
            label += f"\nValue: {repr(node.value)}"
        elif isinstance(node, ast.arg): # For function arguments
            label += f"\nArg: {node.arg}"

        # Add node to graph
        self.dot.node(node_id, label)

        # Connect to parent if not the root
        if hasattr(node, 'parent_id'):
            self.dot.edge(node.parent_id, node_id)

        # Recursively visit children
        for field, value in ast.iter_fields(node):
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, ast.AST):
                        item.parent_id = node_id # Pass parent ID to child
                        self.visit(item)
            elif isinstance(value, ast.AST):
                value.parent_id = node_id # Pass parent ID to child
                self.visit(value)

    def generate_dot(self, tree):
        # Add a custom attribute 'parent_id' to nodes to track their parent for Graphviz edges
        # This is a common pattern when AST nodes don't inherently store parent references.
        # Note: This modifies the AST nodes in place.
        for node in ast.walk(tree):
            for child_node in ast.iter_child_nodes(node):
                child_node.parent_id = self.node_map[node] if node in self.node_map else self.get_new_node_id(node)
                self.node_map[node] = child_node.parent_id # Ensure parent gets ID first

        # Start the visit from the root
        self.visit(tree)
        return self.dot

code = """
class Solution:
    def maxLen(self, n: int, e: List[List[int]], l: str) -> int:
        g = [[] for _ in range(n)]
        for u, v in e:
            g[u].append(v); g[v].append(u)
        q = deque(); vis = set(); ans = 1
        return ans
"""

# Parse the code
tree = ast.parse(code)

# Generate DOT graph
ast_to_dot = AstToDot()
dot_graph = ast_to_dot.generate_dot(tree)

# Render to a file
# You can choose format like 'png', 'svg', 'pdf'
dot_graph.render('ast_image', view=True, format='png') # view=True opens the image after rendering
print("AST image 'ast_image.png' generated successfully!")
