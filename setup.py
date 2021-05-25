from setuptools import setup

setup(
    name="nb-serverproxy-openrefine",
    packages= ['nb_serverproxy_openrefine'],
    version='0.0.1',
    include_package_data=True,
    install_requires=[
        'jupyter-server-proxy',
        'notebook'
    ],
    url="https://github.com/innovationOUtside/nb_serverproxy_openrefine",
    author="Tony Hirst",
    description="tony.hirst@gmail.com",
    entry_points={
        'jupyter_serverproxy_servers': [
            'nb_openrefine = nb_serverproxy_openrefine:setup_openrefine',
        ]
    }
)