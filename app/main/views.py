from flask import Blueprint ,render_template
from app.models import EditableHTML



main_bp = Blueprint('main',__name__)

@main_bp.route('/')
def index():
    return render_template('main/index.html')


@main_bp.route('/about')
def about():
    editable_html_obj = EditableHTML.get_editable_html('about')
    return render_template(
        'main/about.html', editable_html_obj=editable_html_obj)
