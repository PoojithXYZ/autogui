import ast
import graphviz

lazy_segtree_source = """
class lazy_segtree():
    def update(self,k):self.d[k]=self.op(self.d[2*k],self.d[2*k+1])

    def all_apply(self,k,f):
        self.d[k]=self.mapping(f,self.d[k])
        if (k<self.size):self.lz[k]=self.composition(f,self.lz[k])

    def push(self,k):
        self.all_apply(2*k,self.lz[k])
        self.all_apply(2*k+1,self.lz[k])
        self.lz[k]=self.identity

    def __init__(self,V,OP,E,MAPPING,COMPOSITION,ID):
        self.n=len(V)
        self.log=(self.n-1).bit_length()
        self.size=1<<self.log
        self.d=[E for i in range(2*self.size)]
        self.lz=[ID for i in range(self.size)]
        self.e=E
        self.op=OP
        self.mapping=MAPPING
        self.composition=COMPOSITION
        self.identity=ID
        for i in range(self.n):self.d[self.size+i]=V[i]
        for i in range(self.size-1,0,-1):self.update(i)

    def set(self,p,x):
        p+=self.size
        for i in range(self.log,0,-1):self.push(p>>i)
        self.d[p]=x
        for i in range(1,self.log+1):self.update(p>>i)

    def get(self,p):
        p+=self.size
        for i in range(self.log,0,-1):self.push(p>>i)
        return self.d[p]

    def prod(self,l,r):
        if l==r:return self.e
        l+=self.size
        r+=self.size
        for i in range(self.log,0,-1):
            if (((l>>i)<<i)!=l):self.push(l>>i)
            if (((r>>i)<<i)!=r):self.push(r>>i)
        sml,smr=self.e,self.e
        while(l<r):
            if l&1:
                sml=self.op(sml,self.d[l])
                l+=1
            if r&1:
                r-=1
                smr=self.op(self.d[r],smr)
            l>>=1
            r>>=1
        return self.op(sml,smr)

    def all_prod(self):return self.d[1]

    def apply_point(self,p,f):
        assert 0<=p and p<self.n
        p+=self.size
        for i in range(self.log,0,-1):self.push(p>>i)
        self.d[p]=self.mapping(f,self.d[p])
        for i in range(1,self.log+1):self.update(p>>i)

    def apply(self,l,r,f):
        if l==r:return
        l+=self.size
        r+=self.size
        for i in range(self.log,0,-1):
            if (((l>>i)<<i)!=l):self.push(l>>i)
            if (((r>>i)<<i)!=r):self.push((r-1)>>i)
        l2,r2=l,r
        while(l<r):
            if (l&1):
                self.all_apply(l,f)
                l+=1
            if (r&1):
                r-=1
                self.all_apply(r,f)
            l>>=1
            r>>=1
        l,r=l2,r2
        for i in range(1,self.log+1):
            if (((l>>i)<<i)!=l):self.update(l>>i)
            if (((r>>i)<<i)!=r):self.update((r-1)>>i)

    def max_right(self,l,g):
        if l==self.n:return self.n
        l+=self.size
        for i in range(self.log,0,-1):self.push(l>>i)
        sm=self.e
        while(1):
            while(l%2==0):l>>=1
            if not(g(self.op(sm,self.d[l]))):
                while(l<self.size):
                    self.push(l)
                    l=(2*l)
                    if (g(self.op(sm,self.d[l]))):
                        sm=self.op(sm,self.d[l])
                        l+=1
                return l-self.size
            sm=self.op(sm,self.d[l])
            l+=1
            if (l&-l)==l:break
        return self.n

    def min_left(self,r,g):
        if r==0:return 0
        r+=self.size
        for i in range(self.log,0,-1):self.push((r-1)>>i)
        sm=self.e
        while(1):
            r-=1
            while(r>1 and (r%2)):r>>=1
            if not(g(self.op(self.d[r],sm))):
                while(r<self.size):
                    self.push(r)
                    r=(2*r+1)
                    if g(self.op(self.d[r],sm)):
                        sm=self.op(self.d[r],sm)
                        r-=1
                return r+1-self.size
            sm=self.op(self.d[r],sm)
            if (r&-r)==r:break
        return 0
"""
# Parse the source code into an AST
tree = ast.parse(lazy_segtree_source)

# Dictionary to store method calls: {caller_method: [list_of_callee_methods]}
method_calls = {}

# List of all method names in the class
method_names = []
for node in ast.walk(tree):
    if isinstance(node, ast.ClassDef) and node.name == 'lazy_segtree':
        for item in node.body:
            if isinstance(item, ast.FunctionDef):
                method_names.append(item.name)
        break # Found the class, no need to continue walking

# Populate the method_calls dictionary
for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef):
        caller_method_name = node.name
        called_methods_in_current_func = set()
        for sub_node in ast.walk(node):
            if isinstance(sub_node, ast.Call):
                # Check if it's a method call on 'self'
                if isinstance(sub_node.func, ast.Attribute) and \
                   isinstance(sub_node.func.value, ast.Name) and \
                   sub_node.func.value.id == 'self':
                    callee_method_name = sub_node.func.attr
                    if callee_method_name in method_names:
                        called_methods_in_current_func.add(callee_method_name)
        if called_methods_in_current_func:
            method_calls[caller_method_name] = sorted(list(called_methods_in_current_func))

# Create a Graphviz Digraph
dot = graphviz.Digraph(comment='lazy_segtree Call Graph', graph_attr={'rankdir': 'LR'})

# Add nodes for all methods
for method in method_names:
    dot.node(method, method)

# Add edges based on method calls
for caller, callees in method_calls.items():
    for callee in callees:
        dot.edge(caller, callee)

# Render the graph
# The output will be a .gv file and a .png file (or other specified format)
dot.render('lazy_segtree_call_graph', view=True, format='png') # Uncomment to render and view

# To display in environments that support SVG or if graphviz is installed and path is set
# print(dot.source) # Print the DOT language source
# dot.render('lazy_segtree_call_graph', format='svg', cleanup=True)

# Save the DOT source to a string to provide as output
dot_source_code = dot.source

print(f"Here is the Graphviz DOT source code for the call graph of the lazy_segtree class:\n\n{dot_source_code}")

