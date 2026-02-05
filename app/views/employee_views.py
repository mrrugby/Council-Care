from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy
from ..forms import RepairRequestForm, EmployeeSignUpForm
from ..models import RepairRequest, StatusHistory


class EmployeeSignUpView(CreateView):
    form_class = EmployeeSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Employee'
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        return reverse_lazy('employee_dashboard')


@login_required
def employee_dashboard(request):
    if not request.user.is_employee:
        return redirect('login')
    
    

    user_requests = RepairRequest.objects.filter(employee=request.user.employee)
    recent_requests = user_requests.order_by('-created_at')
    
  
    pending_count = user_requests.filter(status='PENDING').count()
    in_progress_count = user_requests.filter(status='IN_PROGRESS').count()
    completed_count = user_requests.filter(status="COMPLETED").count()
    rejected_count = user_requests.filter(status="REJECTED").count()
    
    return render(request, 'employee/employee_dashboard.html', {
        'recent_requests': recent_requests,
        'pending_count': pending_count,
        'rejected_count': rejected_count,
        'completed_count': completed_count,
        'in_progress_count': in_progress_count
    })
     
    
  

@login_required
def create_repair_request(request):
    if not request.user.is_employee:
        return redirect('login')

    if request.method == 'POST':
        form = RepairRequestForm(request.POST, request.FILES)
        if form.is_valid():
            repair_request = form.save(commit=False)
            repair_request.employee = request.user.employee
            repair_request.save()
            return redirect('employee_dashboard')
    else:
        form = RepairRequestForm()

    context = {'form': form}
    return render(request, 'employee/create_repair_request.html', context)


@login_required
def view_repair_request(request, request_id):
    
    repair_request = get_object_or_404(RepairRequest, id=request_id)
    
 
    status_history = StatusHistory.objects.filter(repair_request=repair_request).order_by('updated_at')
    StatusHistory.objects.create(repair_request=repair_request, status=repair_request.status)

 
    context = {
        'repair_request': repair_request,
        'status_history': status_history,
    }

    return render(request, 'employee/view_repair_request.html', context)