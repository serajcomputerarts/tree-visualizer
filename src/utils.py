"""
Utility Functions
Helper functions for the tree visualizer
"""

import os
import re
from datetime import datetime

def sanitize_filename(text, max_length=50):
    """Convert text to safe filename"""
    # Remove invalid characters
    safe_text = re.sub(r'[^\w\-_\.]', '_', text)
    # Limit length
    if len(safe_text) > max_length:
        safe_text = safe_text[:max_length]
    return safe_text

def ensure_directory(path):
    """Create directory if it doesn't exist"""
    os.makedirs(path, exist_ok=True)

def get_timestamp():
    """Get current timestamp as string"""
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def format_tree_string(tree_string):
    """Format tree string for display"""
    return tree_string.strip().replace(' ', '')

def count_nodes(root):
    """Count total nodes in tree"""
    if not root:
        return 0
    return 1 + sum(count_nodes(child) for child in root.children)

def get_tree_stats(root):
    """Get statistics about the tree"""
    if not root:
        return {"nodes": 0, "depth": 0, "leaves": 0}
    
    def count_leaves(node):
        if node.is_leaf():
            return 1
        return sum(count_leaves(child) for child in node.children)
    
    return {
        "nodes": count_nodes(root),
        "depth": root.get_depth(),
        "leaves": count_leaves(root)
    }