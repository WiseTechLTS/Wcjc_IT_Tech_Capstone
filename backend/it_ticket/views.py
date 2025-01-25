from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ITTicket
from .serializers import ITTicketSerializer

@api_view(['POST'])
def create_ticket(request):
    serializer = ITTicketSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Ticket created successfully!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

import logging
logger = logging.getLogger(__name__)

@api_view(['GET'])
def list_tickets(request):
    logger.info("Received GET request to list tickets.")
    tickets = ITTicket.objects.all()
    logger.info(f"Retrieved {tickets.count()} tickets from the database.")
    serializer = ITTicketSerializer(tickets, many=True)
    logger.info("Serialized tickets successfully.")
    return Response(serializer.data)

@api_view(['POST'])
def create_ticket(request):
    serializer = ITTicketSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Ticket created successfully!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
