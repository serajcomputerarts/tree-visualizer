"""
Basic Examples
Simple usage examples for the tree visualizer
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.visualizer import TreeVisualizer
from config.settings import DEFAULT_SETTINGS

def run_basic_examples():
    """Run basic tree visualization examples"""
    
    # Initialize visualizer
    visualizer = TreeVisualizer(DEFAULT_SETTINGS)
    
    print("Running Basic Examples...")
    print("=" * 50)
    
    # Example 1: Simple binary tree
    print("\n1. Simple Binary Tree:")
    tree1 = "A(B,C)"
    print(f"   Input: {tree1}")
    visualizer.process_tree(tree1)
    
    # Example 2: Tree with three children
    print("\n2. Tree with Multiple Children:")
    tree2 = "Root(Child1,Child2,Child3)"
    print(f"   Input: {tree2}")
    visualizer.process_tree(tree2)
    
    # Example 3: Nested tree
    print("\n3. Nested Tree:")
    tree3 = "A(B(D,E),C(F))"
    print(f"   Input: {tree3}")
    visualizer.process_tree(tree3)
    
    # Example 4: Numeric tree
    print("\n4. Numeric Tree:")
    tree4 = "1(2(4,5),3(6,7))"
    print(f"   Input: {tree4}")
    visualizer.process_tree(tree4)
    
    # Example 5: Single node
    print("\n5. Single Node:")
    tree5 = "Root"
    print(f"   Input: {tree5}")
    visualizer.process_tree(tree5)
    
    print("\n" + "=" * 50)
    print("Basic examples completed!")
    print("Check the output/images/ folder for generated visualizations.")

if __name__ == "__main__":
    run_basic_examples()