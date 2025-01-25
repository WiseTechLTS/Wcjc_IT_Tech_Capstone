from django.shortcuts import render, get_object_or_404, redirect
from .models import WorkOrder
from tickets.models import Ticket

def create_work_order(request, ticket_id):
    ticket = get_object_or_404(Ticket, ticket_id=ticket_id)
    if request.method == "POST":
        work_order = WorkOrder.objects.create(
            ticket=ticket,
            work_performed=request.POST['work_performed'],
            parts_used=request.POST.get('parts_used', ''),
            technician_signature=request.POST['technician_signature'],
            customer_signature=request.POST['customer_signature'],
            on_site_hours=request.POST.get('on_site_hours'),
            date_completed=request.POST.get('date_completed'),
            start_time=request.POST.get('start_time'),
            stop_time=request.POST.get('stop_time'),
        )
        return redirect('work_order_detail', pk=work_order.pk)

    return render(request, 'work_orders/create_work_order.html', {'ticket': ticket})

def work_order_detail(request, pk):
    work_order = get_object_or_404(WorkOrder, pk=pk)
    return render(request, 'work_orders/work_order_detail.html', {'work_order': work_order})

# New View for Viewing a Work Order by Ticket's Unique ID
def work_order_view(request, unique_id):
    # Retrieve the work order using the related ticket's unique ID
    work_order = get_object_or_404(WorkOrder, ticket__unique_id=unique_id)
    return render(request, 'work_orders/work_order_detail.html', {'work_order': work_order})
