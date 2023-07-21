from flask import Blueprint

blueprint = Blueprint(
    'authentication_blueprint',
    __name__,
    static_folder='static',
    template_folder='templates'
    )

route_login='authentication_blueprint.login'