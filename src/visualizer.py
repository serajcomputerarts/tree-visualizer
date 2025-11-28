"""
Tree Visualizer Implementation
Handles the visual representation of trees
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
from datetime import datetime
from .tree_parser import TreeParser

class TreeVisualizer:
    """Main class for tree visualization"""
    
    def __init__(self, settings):
        self.settings = settings
        self.parser = TreeParser()
        self._ensure_output_directory()
    
    def _ensure_output_directory(self):
        """Create output directory if it doesn't exist"""
        os.makedirs(self.settings['output_dir'], exist_ok=True)
        os.makedirs(os.path.join(self.settings['output_dir'], 'images'), exist_ok=True)
    
    def process_tree(self, tree_string):
        """Process a tree string and create visualization"""
        try:
            # Validate format
            is_valid, message = TreeParser.validate_format(tree_string)
            if not is_valid:
                print(f"Invalid format: {message}")
                return False
            
            # Parse tree
            root = self.parser.parse(tree_string)
            if not root:
                print("Could not parse tree")
                return False
            
            # Calculate positions
            self._calculate_positions(root)
            
            # Generate filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"tree_{timestamp}.png"
            filepath = os.path.join(self.settings['output_dir'], 'images', filename)
            
            # Draw tree
            self._draw_tree(root, filepath, tree_string)
            
            return True
            
        except Exception as e:
            print(f"Error processing tree: {e}")
            return False
    
    def _calculate_positions(self, root):
        """Calculate x,y positions for all nodes"""
        if not root:
            return
        
        # Calculate subtree widths
        def calc_width(node):
            if node.is_leaf():
                return 1
            return sum(calc_width(child) for child in node.children)
        
        # Assign positions
        def assign_positions(node, x_start, x_end, level):
            node.y = self.settings['height'] - (level + 1) * self.settings['level_height']
            
            if node.is_leaf():
                node.x = (x_start + x_end) / 2
                return
            
            node.x = (x_start + x_end) / 2
            
            # Calculate child positions
            child_widths = [calc_width(child) for child in node.children]
            total_width = sum(child_widths)
            
            if total_width == 0:
                return
            
            current_x = x_start
            available_width = x_end - x_start
            
            for i, child in enumerate(node.children):
                child_proportion = child_widths[i] / total_width
                child_start = current_x
                child_end = current_x + (child_proportion * available_width)
                
                assign_positions(child, child_start, child_end, level + 1)
                current_x = child_end
        
        margin = self.settings['margin']
        assign_positions(root, margin, self.settings['width'] - margin, 0)
    
    def _draw_tree(self, root, filepath, original_string):
        """Draw the tree and save as image"""
        # Setup figure
        dpi = 100
        fig = plt.figure(figsize=(self.settings['width']/dpi, self.settings['height']/dpi), dpi=dpi)
        ax = fig.add_subplot(111)
        
        # Configure axes
        ax.set_xlim(0, self.settings['width'])
        ax.set_ylim(0, self.settings['height'])
        ax.set_aspect('equal')
        ax.axis('off')
        fig.patch.set_facecolor('white')
        
        # Draw tree
        self._draw_node_recursive(ax, root)
        
        # Add title
        ax.text(self.settings['width']/2, self.settings['height'] - 30, 
               f"Tree: {original_string}", 
               ha='center', va='top', fontsize=16, fontweight='bold')
        
        # Save image
        plt.tight_layout()
        plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
        plt.savefig(filepath, dpi=dpi, bbox_inches='tight', 
                   pad_inches=0, facecolor='white')
        plt.show()
        
        print(f"Image saved: {filepath}")
    
    def _draw_node_recursive(self, ax, node):
        """Recursively draw nodes and edges"""
        if not node:
            return
        
        # Draw edges to children
        for child in node.children:
            ax.plot([node.x, child.x], [node.y, child.y], 
                   'k-', linewidth=2, zorder=1)
            self._draw_node_recursive(ax, child)
        
        # Draw node
        circle = plt.Circle((node.x, node.y), self.settings['node_radius'], 
                          facecolor='white', edgecolor='black', 
                          linewidth=2, zorder=2)
        ax.add_patch(circle)
        
        # Add text
        ax.text(node.x, node.y, str(node.value), 
               ha='center', va='center', fontsize=12, 
               fontweight='bold', zorder=3)