from flask import Flask,render_template,jsonify,json,redirect,url_for
from config import Config
import requests

print('FLASK_ENV:{}'.format(Config.FLASK_ENV))
print('DEBUG:{}'.format(Config.DEBUG))
print('API_KEY:{}'.format(Config.API_KEY))
print('HOSTNAME:{}'.format(Config.HOSTNAME))
print('PORT:{}'.format(Config.PORT))
print('STATIC_FOLDER:{}'.format(Config.STATIC_FOLDER))

print()

app = Flask(__name__,template_folder='templates')


@app.route('/',methods=['GET','POST'])

def jokes():
    #handles a request first:
    api_url ='https://api.chucknorris.io/jokes/random'
    response = requests.get(api_url).json()
    value = response["value"]
    return render_template("jokes.html",value=value)



if __name__ == '__main':
    app.run()


