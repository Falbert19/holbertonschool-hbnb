#!/usr/bin/python3
from flask_restx import Namespace, Resource, fields
from app.services import facade
from app.models.user import User

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='Password of the user')
})

@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
        user_data = api.payload

        # check if email exists
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400
        
        #create the new user
        new_user = {
            "first_name": user_data['first_name'],
            "last_name": user_data['last_name'],
            "email": user_data['email'],
            "password": user_data['password']
        }
        new_user.hash_password(user_data['password'])

        #saves the new user
        facade.create_user(new_user)
        return {'id': new_user.id, 'message': 'User succesfully created'}, 201

    @api.route('/<user_id>')
    class UserResource(Resource):
        @api.response(200, 'User details retrieved successfully')
        @api.response(404, 'User not found')
        def get(self, user_id):
            """Get user details by ID"""
            user = facade.get_user(user_id)
            if not user:
                return {'error': 'User not found'}, 404
            return {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email
            }, 200
