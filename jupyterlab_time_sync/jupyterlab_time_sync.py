"""Main module."""

from notebook.utils import url_path_join
from notebook.base.handlers import IPythonHandler

import subprocess

import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

class TimeSyncHandler(IPythonHandler):
    def get(self):
        self.finish('Use POST to set time')

    def post(self):
        data = self.get_json_body()
        log.debug(data)
        # NOTE: only works on linux
        subprocess.run(['sudo', 'date', '-s', data['timestamp']])
        subprocess.run(['sudo', 'timedatectl', 'set-timezone', data['timezone']])
        self.finish('test response')

def load_jupyter_server_extension(nb_server_app):
    """
    Called when the extension is loaded.

    Args:
        nb_server_app (NotebookWebApplication): handle to the Notebook webserver instance.
    """
    web_app = nb_server_app.web_app
    host_pattern = '.*$'
    route_pattern = url_path_join(web_app.settings['base_url'], '/jupyterlab_time_sync')
    web_app.add_handlers(host_pattern, [(route_pattern, TimeSyncHandler)])
