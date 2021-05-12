from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor


#db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # app.config['SECRET_KEY'] = 'thisismysecretkeydonotstealit'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    #
    # db.init_app(app)
    mysql = MySQL(cursorclass=DictCursor)
    app.config['MYSQL_DATABASE_HOST'] = 'db'
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
    app.config['MYSQL_DATABASE_PORT'] = 3306
    app.config['MYSQL_DATABASE_DB'] = 'citiesData'
    mysql.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .app import app as main_blueprint
    app.register_blueprint(main_blueprint)

    return app