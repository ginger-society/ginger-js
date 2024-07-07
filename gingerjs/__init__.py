import os
from .js_bridge import JSBridge
from .create_app.routes.flask import define_routes

def prepare_bridge(**kwargs):
    bridge = JSBridge()
    bridge.initialize(debug= kwargs.get("debug",False))
    return bridge

def add_url_rules(root_folder,app,**kwargs):
    bridge = prepare_bridge(**kwargs)
    
    api_routes = os.path.join(root_folder,"api")
    define_routes(app,api_routes,"api",bridge,debug=kwargs.get("debug",False))

    view_routes = root_folder
    define_routes(app,view_routes,"view",bridge,debug=kwargs.get("debug",False))
