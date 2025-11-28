"""
Unit Tests for Tree Parser
Tests the parsing functionality
"""

import unittest
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from tree_parser import TreeParser
from tree_node import TreeNode

class TestTreeParser(unittest.TestCase):
    """Test cases for TreeParser class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.parser = TreeParser()
    
    def test_simple_node(self):
        """Test parsing a single node"""
        root = self.parser.parse("A")
        self.assertIsNotNone(root)
        self.assertEqual(root.value, "A")
        self.assertEqual(len(root.children), 0)
    
    def test_simple_tree(self):
        """Test parsing a simple tree with children"""
        root = self.parser.parse("A(B,C)")
        self.assertIsNotNone(root)
        self.assertEqual(root.value, "A")
        self.assertEqual(len(root.children), 2)
        self.assertEqual(root.children[0].value, "B")
        self.assertEqual(root.children[1].value, "C")
    
    def test_complex_tree(self):
        """Test parsing a complex nested tree"""
        root = self.parser.parse("8(3(1,6(4,7)),10(14(13)))")
        self.assertIsNotNone(root)
        self.assertEqual(root.value, "8")
        self.assertEqual(len(root.children), 2)
        
        # Check left subtree
        left_child = root.children[0]
        self.assertEqual(left_child.value, "3")
        self.assertEqual(len(left_child.children), 2)
        self.assertEqual(left_child.children[0].value, "1")
        self.assertEqual(left_child.children[1].value, "6")
        
        # Check nested children
        six_node = left_child.children[1]
        self.assertEqual(len(six_node.children), 2)
        self.assertEqual(six_node.children[0].value, "4")
        self.assertEqual(six_node.children[1].value, "7")
    
    def test_whitespace_handling(self):
        """Test handling of whitespace in input"""
        root = self.parser.parse("  A ( B , C )  ")
        self.assertIsNotNone(root)
        self.assertEqual(root.value, "A")
        self.assertEqual(len(root.children), 2)
        self.assertEqual(root.children[0].value, "B")
        self.assertEqual(root.children[1].value, "C")
    
    def test_empty_input(self):
        """Test handling of empty input"""
        root = self.parser.parse("")
        self.assertIsNone(root)
        
        root = self.parser.parse("   ")
        self.assertIsNone(root)
    
    def test_invalid_format(self):
        """Test handling of invalid formats"""
        with self.assertRaises(ValueError):
            self.parser.parse("A(B,C")  # Missing closing parenthesis
        
        with self.assertRaises(ValueError):
            self.parser.parse("A(B,C))")  # Extra closing parenthesis
    
    def test_format_validation(self):
        """Test format validation function"""
        valid, msg = TreeParser.validate_format("A(B,C)")
        self.assertTrue(valid)
        
        valid, msg = TreeParser.validate_format("A(B,C")
        self.assertFalse(valid)
        
        valid, msg = TreeParser.validate_format("")
        self.assertFalse(valid)
    
    def test_numeric_values(self):
        """Test parsing trees with numeric values"""
        root = self.parser.parse("1(2,3)")
        self.assertIsNotNone(root)
        self.assertEqual(root.value, "1")
        self.assertEqual(root.children[0].value, "2")
        self.assertEqual(root.children[1].value, "3")
    
    def test_mixed_values(self):
        """Test parsing trees with mixed alphanumeric values"""
        root = self.parser.parse("Root(Child1,Child2)")
        self.assertIsNotNone(root)
        self.assertEqual(root.value, "Root")
        self.assertEqual(root.children[0].value, "Child1")
        self.assertEqual(root.children[1].value, "Child2")

if __name__ == '__main__':
    unittest.main()