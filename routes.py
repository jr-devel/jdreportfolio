###############DEPENDENCIES
from flask import *
###############CODING
bp = Blueprint('routes', __name__, url_prefix='/')
#
###############ROUTES
#INDEX
@bp.route('/', methods=['GET'])
def index():
    return render_template('routes/index.html')
#ABOUT
@bp.route('/about_me', methods=['GET'])
def about():
    return render_template('routes/about.html')
#CONTACT
@bp.route('/contact', methods=['GET'])
def contact():
    return render_template('routes/contact.html')
