from passlib.handlers.bcrypt import bcrypt

from Model.BaseModel import BaseModel, EnumField
from peewee import  TextField, CharField, PrimaryKeyField
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
import env


class Student(BaseModel):
    firstname = CharField()
    lastname = CharField()
    father = CharField(default='test')
    brithday = CharField(default='test')
    location_brith = CharField(default='test')
    phone = CharField(default='test')
    mobile = CharField(default='test')
    national_code = CharField(default='1234')
    status = EnumField(choices=['active', 'non_active', 'expulsion', 'alumnus'])
    entry_semester = CharField(default='2')
    img = CharField(default='test')
    address = TextField(default='test')
    student_number = PrimaryKeyField(unique=True)
    id = CharField(11)
    password = CharField(100)

    class Meta:
        db_table = "student"
        order_by = ('student_number',)

    def hash_password(self, password):
        self.password = bcrypt.hash(password)

    def verify_password(self, password):
        return bcrypt.verify(password, self.password)

    def generate_auth_token(self, expiration=600):
        s = Serializer(env.secret_key, expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(env.secret_key)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        try:
            user = Student.get(Student.id == data['id'])
            return user
        except:
            return None

