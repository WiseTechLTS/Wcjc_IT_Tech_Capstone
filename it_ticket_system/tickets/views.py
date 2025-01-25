from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Ticket
from .serializers import TicketSerializer
from django.shortcuts import get_object_or_404, render


@api_view(['POST'])
def create_ticket(request):
    data = request.data.copy()  # Create a mutable copy of request.data
    email = data.get('email')

    # Count existing tickets for the email
    tickets_count = Ticket.objects.filter(email=email).count()
    data['ticket_id'] = tickets_count + 1  # Sequential ticket ID per email

    serializer = TicketSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_tickets(request):
    tickets = Ticket.objects.all()
    serializer = TicketSerializer(tickets, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def ticket_detail(request, ticket_id):
    try:
        ticket = Ticket.objects.get(ticket_id=ticket_id)
    except Ticket.DoesNotExist:
        return Response({"error": "Ticket not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TicketSerializer(ticket, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        ticket.delete()
        return Response({"message": "Ticket deleted"}, status=status.HTTP_204_NO_CONTENT)


def work_order_view(request, unique_id):
    ticket = get_object_or_404(Ticket, unique_id=unique_id)
    return render(request, 'tickets/work_order.html', {'ticket': ticket})
def work_order_list_view(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets/work_order_list.html', {'tickets': tickets})
