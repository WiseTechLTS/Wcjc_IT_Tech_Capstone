import jwt
from datetime import datetime, timedelta
from django.conf import settings

def generate_jwt(email, ticket_id):
    """
    Generates a JSON Web Token (JWT) for tracking a ticket.
    
    Args:
        email (str): The email address of the user.
        ticket_id (int): The unique ID of the ticket.
    
    Returns:
        str: A JWT token as a string.
    """
    payload = {
        'email': email,
        'ticket_id': ticket_id,
        'exp': datetime.utcnow() + timedelta(days=7)  # Token expires in 7 days
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token
