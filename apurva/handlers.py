import json

from jupyter_server.base.handlers import APIHandler
from jupyter_server.base.handlers import JupyterHandler
from jupyter_server.utils import url_path_join
import tornado

IMAGES = [
    'https://picsum.photos/id/1/200/300'
]

class RouteHandler(APIHandler):
    # The following decorator should be present on all verb methods (head, get, post,
    # patch, put, delete, options) to ensure only authorized user can request the
    # Jupyter server
    @tornado.web.authenticated
    def get(self):
        image_url = random.choice(IMAGES)
        # self.finish(json.dumps({
        #     "image_url": image_url
        # }))
        self.finish(json.dumps({"data": "This is /jlab-ext-example/hello endpoint!"}))


def setup_handlers(web_app):
    host_pattern = ".*$"

    base_url = web_app.settings["base_url"]
    route_pattern = url_path_join(base_url, "apurva", "get-example")
    handlers = [(route_pattern, RouteHandler)]
    web_app.add_handlers(host_pattern, handlers)
