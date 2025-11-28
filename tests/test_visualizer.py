"""
Unit Tests for Tree Visualizer
Tests the visualization functionality
"""

import unittest
import tempfile
import os
import sys

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from visualizer import TreeVisualizer
from tree_node import TreeNode
from config.settings import DEFAULT_SETTINGS

class TestTreeVisualizer(unittest.TestCase):
    """Test cases for TreeVisualizer class"""
    
    def setUp(self):
        """Set up test fixtures"""
        # Create temporary directory for test outputs
        self.temp_dir = tempfile.mkdtemp()
        self.test_settings = DEFAULT_SETTINGS.copy()
        self.test_settings['output_dir'] = self.temp_dir
        self.visualizer = TreeVisualizer(self.test_settings)
    
    def tearDown(self):
        """Clean up test fixtures"""
        # Clean up temporary files
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_initialization(self):
        """Test visualizer initialization"""
        self.assertIsNotNone(self.visualizer)
        self.assertEqual(self.visualizer.settings['width'], 1920)
        self.assertEqual(self.visualizer.settings['height'], 1080)
    
    def test_output_directory_creation(self):
        """Test that output directories are created"""
        images_dir = os.path.join(self.temp_dir, 'images')
        self.assertTrue(os.path.exists(images_dir))
    
    def test_simple_tree_processing(self):
        """Test processing a simple tree"""
        result = self.visualizer.process_tree("A(B,C)")
        self.assertTrue(result)
    
    def test_complex_tree_processing(self):
        """Test processing a complex tree"""
        result = self.visualizer.process_tree("8(3(1,6(4,7)),10(14(13)))")
        self.assertTrue(result)
    
    def test_invalid_tree_processing(self):
        """Test processing invalid tree format"""
        result = self.visualizer.process_tree("A(B,C")
        self.assertFalse(result)
    
    def test_empty_tree_processing(self):
        """Test processing empty input"""
        result = self.visualizer.process_tree("")
        self.assertFalse(result)
    
    def test_position_calculation(self):
        """Test position calculation for nodes"""
        root = TreeNode("A")
        root.add_child(TreeNode("B"))
        root.add_child(TreeNode("C"))
        
        self.visualizer._calculate_positions(root)
        
        # Root should be positioned
        self.assertGreater(root.x, 0)
        self.assertGreater(root.y, 0)
        
        # Children should be positioned
        for child in root.children:
            self.assertGreater(child.x, 0)
            self.assertGreater(child.y, 0)
            self.assertLess(child.y, root.y)  # Children below parent

if __name__ == '__main__':
    unittest.main()