__version__="0.0.2"

import os
from pathlib import Path

# Requires openrefine to be on the path as: refine
def setup_openrefine():
    openrefine_path =  os.getenv("REFINE_DIR") if "REFINE_DIR" in os.environ else str(Path.home() / 'openrefine')
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
