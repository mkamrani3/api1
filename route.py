from Controller import CourseController, LoginController


def route(api):
    api.add_resource(CourseController.List, '/course')
    api.add_resource(LoginController.Login, '/login')