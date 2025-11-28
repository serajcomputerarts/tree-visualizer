"""
Configuration Settings
Default settings for the tree visualizer
"""

DEFAULT_SETTINGS = {
    # Image dimensions (1920x1080 as requested)
    'width': 1080,
    'height': 540,
    
    # Node appearance
    'node_radius': 30,
    'node_color': 'white',
    'node_border_color': 'black',
    'node_border_width': 2,
    
    # Text settings
    'font_size': 12,
    'font_weight': 'bold',
    'text_color': 'black',
    
    # Layout settings
    'level_height': 120,
    'margin': 100,
    'min_node_spacing': 80,
    
    # Edge settings
    'edge_color': 'black',
    'edge_width': 2,
    
    # Output settings
    'output_dir': 'output',
    'image_format': 'png',
    'dpi': 100,
    
    # Background
    'background_color': 'white'
}

# Alternative themes
DARK_THEME = DEFAULT_SETTINGS.copy()
DARK_THEME.update({
    'background_color': '#2b2b2b',
    'node_color': '#404040',
    'node_border_color': '#ffffff',
    'text_color': '#ffffff',
    'edge_color': '#ffffff'
})

COLORFUL_THEME = DEFAULT_SETTINGS.copy()
COLORFUL_THEME.update({
    'node_color': '#e3f2fd',
    'node_border_color': '#1976d2',
    'edge_color': '#1976d2'
})