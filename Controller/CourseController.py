from flask_restful import Resource

from Model.Course import Course


class List(Resource):
    def get(self):
        course = Course.select()

        ls = [ dict(
        id  = c.id,
        presentation = c.presentation,
        type = c.type,
        status_prerequisite = c.status_prerequisite,
        name = c.name,
        unit_number = c.unit_number,
        price = c.price,
        list_prerequisite = c.list_prerequisite
        )for c in course
        ]
        return dict(course=ls)

