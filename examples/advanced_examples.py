"""
Advanced Examples
Complex tree visualization examples
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.visualizer import TreeVisualizer
from config.settings import DEFAULT_SETTINGS
from config.themes import THEMES

def run_advanced_examples():
    """Run advanced tree visualization examples"""
    
    print("Running Advanced Examples...")
    print("=" * 50)
    
    # Example 1: Complex binary search tree
    print("\n1. Binary Search Tree:")
    bst = "8(3(1,6(4,7)),10(14(13)))"
    print(f"   Input: {bst}")
    visualizer = TreeVisualizer(DEFAULT_SETTINGS)
    visualizer.process_tree(bst)
    
    # Example 2: Deep tree
    print("\n2. Deep Linear Tree:")
    deep_tree = "A(B(C(D(E(F)))))"
    print(f"   Input: {deep_tree}")
    visualizer.process_tree(deep_tree)
    
    # Example 3: Wide tree
    print("\n3. Wide Tree:")
    wide_tree = "Root(A,B,C,D,E,F,G,H)"
    print(f"   Input: {wide_tree}")
    visualizer.process_tree(wide_tree)
    
    # Example 4: Unbalanced tree
    print("\n4. Unbalanced Tree:")
    unbalanced = "1(2(4(8,9),5(10,11)),3(6,7(12(24,25))))"
    print(f"   Input: {unbalanced}")
    visualizer.process_tree(unbalanced)
    
    # Example 5: Tree with descriptive names
    print("\n5. Organizational Chart:")
    org_chart = "CEO(CTO(DevManager(Dev1,Dev2),QAManager(QA1)),CFO(Accountant1,Accountant2))"
    print(f"   Input: {org_chart}")
    visualizer.process_tree(org_chart)
    
    # Example 6: Mathematical expression tree
    print("\n6. Expression Tree:")
    expression = "+(*(a,b),/(c,d))"
    print(f"   Input: {expression}")
    visualizer.process_tree(expression)
    
    print("\n" + "=" * 50)
    print("Advanced examples completed!")
    print("Check the output/images/ folder for generated visualizations.")

def demonstrate_themes():
    """Demonstrate different visual themes"""
    print("\nDemonstrating Visual Themes...")
    print("=" * 50)
    
    sample_tree = "A(B(D,E),C(F,G))"
    
    for theme_name, theme_data in THEMES.items():
        print(f"\nGenerating with {theme_data['name']} theme...")
        
        # Create settings with theme
        settings = DEFAULT_SETTINGS.copy()
        settings.update(theme_data['settings'])
        
        visualizer = TreeVisualizer(settings)
        visualizer.process_tree(sample_tree)

if __name__ == "__main__":
    run_advanced_examples()
    demonstrate_themes()