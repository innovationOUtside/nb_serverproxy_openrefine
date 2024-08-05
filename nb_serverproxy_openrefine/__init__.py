__version__="0.0.9"

import os
from pathlib import Path

# Requires openrefine to be on the path as: refine
def setup_openrefine():
    openrefine_path =  os.getenv("REFINE_DIR") if "REFINE_DIR" in os.environ else str(Path.home() / 'openrefine')
    openrefine_domain =  os.getenv("REFINE_DOMAIN") if "REFINE_DOMAIN" in os.environ else str('*')
    openrefine_exe_path = os.getenv("OPENREFINE_PATH") if "OPENREFINE_PATH" in os.environ else ''
    openrefine_exe_path = f"{openrefine_exe_path}/refine" if openrefine_exe_path else 'refine'
    if not os.path.exists(openrefine_path):
        os.makedirs(openrefine_path)
    return {
        'command': [openrefine_exe_path, '-p', '{port}','-d', openrefine_path, '-H', openrefine_domain],
        'environment': {},
        'timeout': 120,
        'launcher_entry': {
            'title': 'OpenRefine',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'openrefine.svg')
        }
    }
