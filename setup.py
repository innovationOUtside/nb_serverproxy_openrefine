from setuptools import setup
import os

def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()

setup(
    name="nb-serverproxy-openrefine",
    packages= ['nb_serverproxy_openrefine'],
    version='0.0.2',
    include_package_data=True,
    install_requires=[
        'jupyter-server-proxy',
        'notebook'
    ],
    #extras_require={'pyclient':['git+https://github.com/dbutlerdb/refine-client-py']},
    #extras_require={'pyclient':['openrefine-client']},
    url="https://github.com/innovationOUtside/nb_serverproxy_openrefine",
    author="Tony Hirst",
    description="Jupyer server proxy wrapper for Open Refine",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    entry_points={
        'jupyter_serverproxy_servers': [
            'nb_openrefine = nb_serverproxy_openrefine:setup_openrefine',
        ]
    }
)