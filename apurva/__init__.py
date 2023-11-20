try:
    from ._version import __version__
except ImportError:
    # Fallback when using the package in dev mode without installing
    # in editable mode with pip. It is highly recommended to install
    # the package from a stable release or in editable mode: https://pip.pypa.io/en/stable/topics/local-project-installs/#editable-installs
    import warnings
    warnings.warn("Importing 'apurva' outside a proper installation.")
    __version__ = "dev"
import json
from pathlib import Path
from .handlers import setup_handlers
import random


def test_jupyter_lab_extension():
    names = ["raja", "laxman", "jay", "ajay", "lopo", "tost", "lola", "manish", "Vishal"]
    idx = random.randint(0, len(names) - 1)
    return names[idx]

HERE = Path(__file__).parent.resolve()

with (HERE / "labextension" / "package.json").open() as fid:
    data = json.load(fid)

def _jupyter_labextension_paths():
    return [{
        "src": "labextension",
        "dest": data["name"]
    }]


def _jupyter_server_extension_points():
    return [{
        "module": "apurva"
    }]


def _load_jupyter_server_extension(server_app):
    """Registers the API handler to receive HTTP requests from the frontend extension.

    Parameters
    ----------
    server_app: jupyterlab.labapp.LabApp
        JupyterLab application instance
    """
    setup_handlers(server_app.web_app)
    name = "apurva"
    server_app.log.info(f"Registered {name} server extension")


load_jupyter_server_extension = _load_jupyter_server_extension