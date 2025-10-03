def user_schema(user) -> dict:
    return {
        'id': str(user['_id']),
        'name': str(user['name']),
        'username': str(user['username']),
        'email': str(user['email']),
    }

def user_db_schema(user) -> dict:
    schema = user_schema(user)
    schema['password'] = str(user['password'])
    return schema