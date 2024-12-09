from ninja import NinjaAPI
from . import usuarios

api = NinjaAPI()

# Registrar los routers
api.add_router("/usuarios/", usuarios.router) 