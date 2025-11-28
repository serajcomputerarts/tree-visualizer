#!/usr/bin/env python3
"""
Tree Visualizer - Main Entry Point
Converts parenthetical tree notation to visual representation
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.visualizer import TreeVisualizer
from config.settings import DEFAULT_SETTINGS

def main():
    """Main function to run the tree visualizer"""
    visualizer = TreeVisualizer(DEFAULT_SETTINGS)
    
    print("=" * 50)
    print("Tree Visualizer v1.0")
    print("=" * 50)
    print("Enter tree in parenthetical notation")
    print("Examples:")
    print("  A(B,C) - Simple tree with root A")
    print("  8(3(1,6(4,7)),10(14(13))) - Complex tree")
    print("Type 'quit' to exit")
    print("-" * 50)
    
    while True:
        try:
            tree_input = input("\nEnter tree: ").strip()
            
            if tree_input.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
                
            if not tree_input:
                continue
                
            success = visualizer.process_tree(tree_input)
            if success:
                print("✓ Tree visualization created successfully!")
            else:
                print("✗ Failed to create visualization")
                
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()