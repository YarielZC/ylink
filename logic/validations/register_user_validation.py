from models.user import UserCreate
from fastapi import HTTPException, status
from db.client import db_client
from repositories.user_repository import db_users

def register_user_validate(user: UserCreate):
    # Asegurarse que no existan campos vacios
    if user.name == '':
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Field name cannot be empty')
    if user.username == '':
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Field username cannot be empty')
    if user.email == '':
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Field email cannot be empty')
    if user.password == '':
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Field password cannot be empty')

    # Asegurarse que solo exista un username igual
    found = db_users.find_by_field('username', user.username)

    if found:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail='Username already exists')
    
    # Asegurarse que solo exista un email igual
    found = db_users.find_by_field('email', user.email)

    if found:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail='Email already have a account')
    
    # Asegurarse que la contrasena este entre 8 y 25 caracteres
    if len(user.password) < 8 or len(user.password) > 25:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Password must have a lenght between 8 and 25 characters')

    # Asegurarse que el usuario solo tenga minusculas
    if user.username.lower() != user.username:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Username must be lowercase')

    # Sea un correo valido gmail
    if user.email.find('@gmail.com') == -1 and user.email.islower():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Email must be a correct gmail')