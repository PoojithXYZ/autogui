import ast
import graphviz

class AstToDot(ast.NodeVisitor):
    def __init__(self):
        self.dot = graphviz.Digraph(comment='AST', graph_attr={'rankdir': 'TB'})
        self.node_counter = 0
        self.node_map = {}

    def get_new_node_id(self, node):
        node_id = f"node_{self.node_counter}"
        self.node_counter += 1
        self.node_map[node] = node_id
        return node_id

    def visit(self, node):
        node_id = self.get_new_node_id(node)

        label = type(node).__name__
        if hasattr(node, 'name'):
            label += f"\nName: {node.name}"
        elif hasattr(node, 'id'):
            label += f"\nID: {node.id}"
        elif hasattr(node, 'value'):
            label += f"\nValue: {repr(node.value)}"
        elif isinstance(node, ast.arg):
            label += f"\nArg: {node.arg}"

        self.dot.node(node_id, label)

        if hasattr(node, 'parent_id'):
            self.dot.edge(node.parent_id, node_id)

        for field, value in ast.iter_fields(node):
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, ast.AST):
                        item.parent_id = node_id
                        self.visit(item)
            elif isinstance(value, ast.AST):
                value.parent_id = node_id
                self.visit(value)

    def generate_dot(self, tree):
        for node in ast.walk(tree):
            for child_node in ast.iter_child_nodes(node):
                child_node.parent_id = self.node_map[node] if node in self.node_map else self.get_new_node_id(node)
                self.node_map[node] = child_node.parent_id

        self.visit(tree)
        return self.dot

fib_recursive_code = """
def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)
"""

tree_recursive = ast.parse(fib_recursive_code)
ast_to_dot_recursive = AstToDot()
dot_graph_recursive = ast_to_dot_recursive.generate_dot(tree_recursive)
dot_graph_recursive.render('fib_recursive_ast', view=True, format='png')
print("AST image 'fib_recursive_ast.png' generated successfully!")
