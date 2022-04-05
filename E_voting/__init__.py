from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_manager, LoginManager



app = Flask(__name__)


app.config['DATABASE_URL'] = 'sqlite:///voting.db'
app.config['SECRET_KEY'] = 'd6ac11bed59b75a6bmn4310nvbv4454ab'




bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.login_view = 'authent.login'
login_manager.init_app(app)
login_manager.login_message_category = 'info'



from E_voting.view.routes import views
from E_voting.dashboard.routes import dashbrd
from E_voting.errors.handlers import my_404
from E_voting.result.routes import result_display
from E_voting.admin.routes import admin_panel
from E_voting.authentication.routes import authent


app.register_blueprint(result_display, url_prefix='/')
app.register_blueprint(admin_panel, url_prefix='/')
app.register_blueprint(my_404, url_prefix='/')
app.register_blueprint(authent, url_prefix='/')
app.register_blueprint(dashbrd, url_prefix='/')
app.register_blueprint(views, url_prefix='/')
 


