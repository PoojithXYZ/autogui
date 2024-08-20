import ast
import graphviz

def visualize_ast(file_path):
  """Visualizes the AST of a Python file.

  Args:
    file_path: Path to the Python file.
  """

  with open(file_path, 'r') as f:
    code = f.read()

  try:
    tree = ast.parse(code)
  except SyntaxError as e:
    print(f"Syntax error in file: {file_path}")
    print(e)
    return

  graph = graphviz.Digraph()
  graph.attr(rankdir='TB')  # Top-to-bottom layout

  def add_nodes_and_edges(node, parent_name=None):
    node_name = str(id(node))
    graph.node(node_name, str(type(node).__name__))

    if parent_name:
      graph.edge(parent_name, node_name)

    for child in ast.iter_child_nodes(node):
      add_nodes_and_edges(child, node_name)

  add_nodes_and_edges(tree)
  graph.render('ast_visualization.gv', view=True)

if __name__ == '__main__':
  file_path = input("Enter the path to the Python file: ")
  visualize_ast(file_path)
