from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from ..models import RepairRequest
from ..forms import TechnicanSignUpForm, RepairRequestCommentForm
from django.db.models import Q


class TechnicianSignUpView(CreateView):
    form_class = TechnicanSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Technician'
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        return reverse_lazy('technician_dashboard')


@login_required
def technician_dashboard(request):
    if not request.user.is_technician:
        return redirect('login')

    repair_requests = RepairRequest.objects.filter(
        Q(technician=request.user.technician) | Q(technician__isnull=True)
        ).order_by('-created_at')

    context = {
        'repair_requests': repair_requests,
    }
    return render(request, 'technician/technician_dashboard.html', context)


@login_required
def update_task_status(request, request_id, employee_username):
    if not request.user.is_technician:
        return redirect('login')

    repair_request = get_object_or_404(RepairRequest, id=request_id)
    if repair_request.technician !=request.user.technician:
        return redirect('technician_dashboard')
    employee = repair_request.employee
    if employee.user.username != employee_username:
        return redirect('login')
    
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        repair_request.status = new_status
        repair_request.save()
        return redirect('technician_dashboard')

    context = {
        'repair_request': repair_request,
        'employee' : employee,
    }
    return render(request, 'technician/update_task_status.html', context)


@login_required
def technician_add_comment(request, repair_request_id):
    repair_request = get_object_or_404(RepairRequest, id=repair_request_id)
    
    if not hasattr(request.user, 'technician'):
        return HttpResponseForbidden("Only technicians can comment on this")
    
    return handle_comment_logic(request, repair_request)


def handle_comment_logic(request, repair_request):
    if request.method == 'POST':
        form = RepairRequestCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.repair_request = repair_request
            comment.user = request.user
            comment.save()
            return redirect('repair_request_detail', repair_request_id=repair_request.id)
        
    else:
        form = RepairRequestCommentForm()
        
    return render(request, 'add_comment.html', {'form' : form, 'repair_request' : repair_request})