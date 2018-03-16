from flask import Flask
from flask_restful import Api
from Controller import CourseController
import env

app = Flask(__name__)
api = Api(app)

api.add_resource(CourseController.List,'/course')

if __name__ == '__main__':

    app.run(env.HOST, env.PORT, env.DEBUG)