# jupyterlab_time_sync

Jupyterlab Extension to sync Server time with Client time


## Requirements

* JupyterLab = 1.2.*

May work with other versions, may require modifying dependency versions in `package.json`.

## Install

JupyterLab client extension:

```bash
# from repository root directory
jupyter labextension install
```

JupyterLab server extension:
```bash
# from repository root directory
pip install .
```

Then enable the server extension by editing `jupyter_notebook_config.json` (usually located at `~/.jupyter/jupyter_notebook_config.json`) and adding `"jupyterlab_time_sync": true` to `NotebookApp.nbserver_extensions`, e.g. (merge with existing content):

```json
{
  "NotebookApp": {
    "nbserver_extensions": {
      "jupyterlab_time_sync": true
    }
  }
}
```

### Uninstall

```bash
jupyter labextension uninstall jupyterlab_time_sync
pip uninstall jupyterlab_time_sync
```

Also remove the line from `jupyter_notebook_config.json`.
