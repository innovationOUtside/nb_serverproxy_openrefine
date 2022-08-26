# nb_serverproxy_openrefine
Jupyter server proxy for OpenRefine

> Based on the original https://github.com/psychemedia/jupyterserverproxy-openrefine which has some docs, although the reponame/install instructions will need updating for this repo. *I will pop the package on PyPi at some point.*

Jupyter-server-proxy config for running OpenRefine.

Install as:

```bash
pip install nb-serverproxy-openrefine
```

To install directly from this repo:

```bash
pip install git+https://github.com/innovationOUtside/nb_serverproxy_openrefine.git
```

Open to Notebook homepage: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/innovationOUtside/nb_serverproxy_openrefine/main)

Open to OpenRefine: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/innovationOUtside/nb_serverproxy_openrefine/main?urlpath=openrefine)

Open to Jupyterlab: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/innovationOUtside/nb_serverproxy_openrefine/main?urlpath=lab)

OpenRefine can now be started and launched from the notebook homepage New menu:

![](images/openrefine_new.png)

Or from the JupyterLab launcher:

![](images/openrefine_lab.png)

The OpenRefine client can be found on the `openrefine` path (the port number is allocated dynamically).

Calling the path directly (eg starting MyBinder with the path `openrefine`, or adding `?urlpath=openrefine` to the Binder URL) will launch the Binder container directly into the OpenRefine GUI application.

![](images/OpenRefine_binder.png)

The directory path into which the OpenRefine project files are saved is `$HOME/openrefine` by default, although you can trump it via the `$REFINE_DIR` global variable:

```python
openrefine_path =  os.getenv("REFINE_DIR") if "REFINE_DIR" in os.environ else str(Path.home() / 'openrefine')
```

The host openrefine will use is `127.0.0.1` by default. This can be overriden with the `$REFINE_DOMAIN` global variable

> Early original work on getting OpenRefine running in MyBinder was done by @betatim ([betatim/openrefineder](https://github.com/betatim/openrefineder)) and @yuvipanda helped me get my head round various bits of [jupyterhub/jupyter-server-proxy/](https://github.com/jupyterhub/jupyter-server-proxy/) which is key to proxying web services via Jupyter. @manics PR for handling predefined, rather than allocated, port mappings also made life much easier...

## Python Client

A Python client is also available for working with OpenRefine:

- [`opencultureconsulting/openrefine-client`](https://github.com/opencultureconsulting/openrefine-client) looks to be the best supported but seems to rely on Python 2.7; there is a [currently failing PR to add Python3 support](https://github.com/opencultureconsulting/openrefine-client/pull/8).
- [`dbutlerdb /refine-client-py`](git+https://github.com/dbutlerdb/refine-client-py) works with Python3 but lags `opencultureconsulting /openrefine-client`

*Using the client requires Open Refine to be running.* `TO DO: should we hardwire the port? Else how do we know where to connect?`:

*When the client works with Python3 I will add it as an optional dependency to this package.*

