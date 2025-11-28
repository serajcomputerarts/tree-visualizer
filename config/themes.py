"""
Visual Themes
Different visual themes for tree visualization
"""

THEMES = {
    'default': {
        'name': 'Default',
        'description': 'Clean white background with black nodes',
        'settings': {
            'background_color': 'white',
            'node_color': 'white',
            'node_border_color': 'black',
            'text_color': 'black',
            'edge_color': 'black'
        }
    },
    
    'dark': {
        'name': 'Dark Mode',
        'description': 'Dark background with light nodes',
        'settings': {
            'background_color': '#2b2b2b',
            'node_color': '#404040',
            'node_border_color': '#ffffff',
            'text_color': '#ffffff',
            'edge_color': '#ffffff'
        }
    },
    
    'blue': {
        'name': 'Blue Theme',
        'description': 'Blue color scheme',
        'settings': {
            'background_color': 'white',
            'node_color': '#e3f2fd',
            'node_border_color': '#1976d2',
            'text_color': '#0d47a1',
            'edge_color': '#1976d2'
        }
    },
    
    'green': {
        'name': 'Green Theme',
        'description': 'Nature-inspired green theme',
        'settings': {
            'background_color': '#f1f8e9',
            'node_color': '#c8e6c9',
            'node_border_color': '#2e7d32',
            'text_color': '#1b5e20',
            'edge_color': '#2e7d32'
        }
    }
}

def get_theme(theme_name):
    """Get theme settings by name"""
    return THEMES.get(theme_name, THEMES['default'])

def list_themes():
    """List all available themes"""
    return [(name, theme['name'], theme['description']) 
            for name, theme in THEMES.items()]