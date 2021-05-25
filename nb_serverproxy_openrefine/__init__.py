__version__="0.0.1"

import os

# Requires openrefine to be on the path as: refine
def setup_openrefine():
    openrefine_path = '~/openrefine'
    if not os.path.exists(openrefine_path):
        os.makedirs(openrefine_path)
    return {
        'command': ['refine', '-p', '{port}','-d', openrefine_path],
        'environment': {},
        'launcher_entry': {
            'title': 'OpenRefine',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'openrefine.svg')
        }
    }
