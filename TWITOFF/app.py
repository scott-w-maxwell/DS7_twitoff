"""Main application for twitoff"""
from decouple import config
from flask import Flask, render_template, request
from .models import DB, User
from .twitter import add_or_update_user
def create_app():
    """creates and configures an instance of a flask app"""
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    # app.config['ENV'] = config('ENV') #change this later to "production"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #gets rid of overhead warning 

    DB.init_app(app)

    @app.route('/')
    def root():
        users = User.query.all() #Grabs all the users and puts them in "users"
        return render_template('base.html', title = 'Home', users = users)
    
    @app.route('/user',methods=['POST','GET'])
    @app.route('/user/<name>', methods=['GET'])
    def user(name=None,messase=''):
        try:
            if request.method == 'POST':
                add_or_update_user(name)
                message="User {} successfully added!".format(name)
            tweets = User.query.filter(user.name == name).one().tweets
        except Exception as e:
            message = "Error adding {}: {}".formate(name,e)
            tweets=[]
        return render_template('user.html',title=name, tweets=tweets,message=message)


    #remove for final product
    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='DB Reset', users=[])
    return app