import json

from jupyter_server.base.handlers import APIHandler
from jupyter_server.utils import url_path_join
import tornado

import subprocess
import os

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
        if 'LOCALTIME_PATH' in os.environ and 'TIMEZONE_PATH' in os.environ:
            # don't use sudo or timedatectl
            subprocess.run(['date', '-s', data['timestamp']])
            with open(os.environ['TIMEZONE_PATH'], 'w+') as f:
                f.write(data['timezone'])
            subprocess.run(['rm', os.environ['LOCALTIME_PATH']]) # in case it is a symbolic link
            subprocess.run([
                'cp',
                os.path.join('/usr/share/zoneinfo/', data['timezone']),
                os.environ['LOCALTIME_PATH']])
        else:
            subprocess.run(['sudo', 'date', '-s', data['timestamp']])
            subprocess.run(['sudo', 'timedatectl', 'set-timezone', data['timezone']])
        self.finish(json.dumps({'message': 'time updated'}))


def setup_handlers(web_app):
    host_pattern = ".*$"

    base_url = web_app.settings["base_url"]
    route_pattern = url_path_join(base_url, "jupyterlab_time_sync")
    handlers = [(route_pattern, RouteHandler)]
    web_app.add_handlers(host_pattern, handlers)
