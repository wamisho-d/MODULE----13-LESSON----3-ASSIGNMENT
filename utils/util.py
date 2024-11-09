# Task 2: Implement JWT Token Generation: First, ensure we have pyjwt installed by adding it to your requirements.txt:

# PyJWT==2.x.x

# Now, create the utils/util.py file:

import jwt
import datetime

SECRET_KEY = 'your_secret_key'  # Ensure this key is secure and not exposed

def encode_token(user_id):
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),  # Token expiration: 1 day
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    except Exception as e:
        return e
