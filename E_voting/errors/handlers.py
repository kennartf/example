from flask import Blueprint
from flask import render_template


my_404 = Blueprint('my_404', __name__)


@my_404.app_errorhandler(404)
def page_not_found(error):
    return render_template('404_error_page.html'), 404


# @my_404.app_errorhandler(403)
# def page_not_found(error):
#     return render_template('403.html'), 403


@my_404.app_errorhandler(500)
def page_not_found(error):
    return render_template('500_error_page.html'), 500