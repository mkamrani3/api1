from flask import Flask
from flask_restful import Api

import route
import env

app = Flask(__name__)
api = Api(app)

route.route(api)

if __name__ == '__main__':

    app.run(env.HOST, env.PORT, env.DEBUG)