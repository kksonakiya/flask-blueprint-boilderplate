from flask import Blueprint



blueprint = Blueprint(
    'home_blueprint',
    __name__,
    static_folder='static',
    template_folder='templates'
   
   
)
