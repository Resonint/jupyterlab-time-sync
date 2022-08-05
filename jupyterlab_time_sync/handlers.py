import json

from jupyter_server.base.handlers import APIHandler
from jupyter_server.utils import url_path_join
import tornado

import subprocess

import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

class RouteHandler(APIHandler):
    # The following decorator should be present on all verb methods (head, get, post,
    # patch, put, delete, options) to ensure only authorized user can request the
    # Jupyter server
    @tornado.web.authenticated
    def get(self):
        self.finish(json.dumps({'message': 'Use POST to set time'}))

    @tornado.web.authenticated
    def post(self):
        data = self.get_json_body()
        log.debug(data)
        # NOTE: only works on linux
        subprocess.run(['sudo', 'date', '-s', data['timestamp']])
        subprocess.run(['sudo', 'timedatectl', 'set-timezone', data['timezone']])
        self.finish(json.dumps({'message': 'time updated'}))


def setup_handlers(web_app):
    host_pattern = ".*$"

    base_url = web_app.settings["base_url"]
    route_pattern = url_path_join(base_url, "jupyterlab_time_sync")
    handlers = [(route_pattern, RouteHandler)]
    web_app.add_handlers(host_pattern, handlers)
