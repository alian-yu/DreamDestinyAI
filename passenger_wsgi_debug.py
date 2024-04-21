import importlib.util
from wsgiref.simple_server import make_server

import os
import sys


sys.path.insert(0, os.path.dirname(__file__))

spec = importlib.util.spec_from_file_location('wsgi', 'main.py')
wsgi = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wsgi)

application = wsgi.application

# Create a simple WSGI server
with make_server('', 80, application) as httpd:
    print("Serving on port 80...")
    # Serve until process is killed
    httpd.serve_forever()