"""
Tree Parser Implementation
Parses parenthetical notation into tree structures
"""

import re
from .tree_node import TreeNode

class TreeParser:
    """Parser for parenthetical tree notation"""
    
    def __init__(self):
        self.position = 0
        self.input_string = ""
    
    def parse(self, tree_string):
        """
        Parse a tree from parenthetical notation
        Format: A(B,C) means A is root with children B and C
        """
        self.input_string = tree_string.strip()
        self.position = 0
        
        if not self.input_string:
            return None
        
        try:
            return self._parse_node()
        except Exception as e:
            raise ValueError(f"Invalid tree format: {e}")
    
    def _parse_node(self):
        """Parse a single node and its children"""
        # Skip whitespace
        self._skip_whitespace()
        
        if self.position >= len(self.input_string):
            return None
        
        # Parse node value
        value = self._parse_value()
        if not value:
            return None
        
        node = TreeNode(value)
        
        # Check for children
        self._skip_whitespace()
        if (self.position < len(self.input_string) and 
            self.input_string[self.position] == '('):
            
            self.position += 1  # Skip '('
            self._parse_children(node)
            
            # Expect closing parenthesis
            self._skip_whitespace()
            if (self.position >= len(self.input_string) or 
                self.input_string[self.position] != ')'):
                raise ValueError("Missing closing parenthesis")
            self.position += 1  # Skip ')'
        
        return node
    
    def _parse_value(self):
        """Parse node value (everything until '(', ')', or ',')"""
        start = self.position
        
        while (self.position < len(self.input_string) and 
               self.input_string[self.position] not in '(),'):
            self.position += 1
        
        value = self.input_string[start:self.position].strip()
        return value if value else None
    
    def _parse_children(self, parent):
        """Parse children of a node"""
        while True:
            self._skip_whitespace()
            
            if (self.position >= len(self.input_string) or 
                self.input_string[self.position] == ')'):
                break
            
            if self.input_string[self.position] == ',':
                self.position += 1
                continue
            
            child = self._parse_node()
            if child:
                parent.add_child(child)
    
    def _skip_whitespace(self):
        """Skip whitespace characters"""
        while (self.position < len(self.input_string) and 
               self.input_string[self.position].isspace()):
            self.position += 1
    
    @staticmethod
    def validate_format(tree_string):
        """Validate parenthetical notation format"""
        if not tree_string.strip():
            return False, "Empty string"
        
        # Check balanced parentheses
        level = 0
        for char in tree_string:
            if char == '(':
                level += 1
            elif char == ')':
                level -= 1
                if level < 0:
                    return False, "Unmatched closing parenthesis"
        
        if level != 0:
            return False, "Unmatched opening parenthesis"
        
        return True, "Valid format"