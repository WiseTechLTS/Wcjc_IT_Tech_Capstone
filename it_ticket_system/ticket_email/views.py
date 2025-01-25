from django.http import JsonResponse
from django.core.mail import send_mail
from .models import Ticket
from .utils import generate_jwt

def create_ticket(request):
    """
    Handles the creation of a new ticket based on an email request.
    Returns a JSON Web Token (JWT) to the user for tracking.
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        description = request.POST.get('description')

        if not email or not subject or not description:
            return JsonResponse({'error': 'All fields are required.'}, status=400)

        # Create a new ticket
        ticket = Ticket.objects.create(email=email, subject=subject, description=description)
        
        # Generate a JWT token for the ticket
        token = generate_jwt(email, ticket.id)
        ticket.token = token
        ticket.save()

        # Send the JWT token back to the user via email
        send_mail(
            subject='Your Ticket Has Been Created',
            message=f'Your ticket has been created successfully. Your tracking token is: {token}',
            from_email='support@example.com',
            recipient_list=[email],
            fail_silently=False,
        )

        return JsonResponse({'message': 'Ticket created successfully.', 'token': token}, status=201)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)
