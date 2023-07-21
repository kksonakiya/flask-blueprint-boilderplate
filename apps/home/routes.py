
from flask import render_template
from apps.home import blueprint

@blueprint.route('/')
@blueprint.route('/home')
def home():
    
    return render_template('home.html', title='Home')

