"""
Tree Node Implementation
Defines the basic structure for tree nodes
"""

class TreeNode:
    """Represents a node in a tree structure"""
    
    def __init__(self, value):
        self.value = str(value).strip()
        self.children = []
        self.x = 0
        self.y = 0
        self.parent = None
    
    def add_child(self, child):
        """Add a child node"""
        if isinstance(child, TreeNode):
            child.parent = self
            self.children.append(child)
        else:
            child_node = TreeNode(child)
            child_node.parent = self
            self.children.append(child_node)
    
    def is_leaf(self):
        """Check if node is a leaf (has no children)"""
        return len(self.children) == 0
    
    def get_depth(self):
        """Get the depth of the subtree rooted at this node"""
        if self.is_leaf():
            return 1
        return 1 + max(child.get_depth() for child in self.children)
    
    def get_width(self):
        """Get the width of the subtree (number of leaves)"""
        if self.is_leaf():
            return 1
        return sum(child.get_width() for child in self.children)
    
    def __str__(self):
        return f"TreeNode({self.value})"
    
    def __repr__(self):
        return self.__str__()