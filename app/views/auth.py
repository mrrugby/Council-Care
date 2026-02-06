import os
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views import View
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from ..forms import EmployeeSignUpForm, TechnicanSignUpForm, AdminSignUpForm
from django.contrib.auth import authenticate, login


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    
    def get_initial(self):
        
        initial = super().get_initial()
        if self.request.GET.get('demo') == '1':
            initial['username'] = os.environ.get('DEMO_USERNAME', 'demo')
            
            
        return initial
    
    def get_success_url(self):
        user = self.request.user
        if user.is_admin:
            return reverse_lazy('admin_dashboard')
        elif user.is_technician:
            return reverse_lazy('technician_dashboard')
        elif user.is_employee:
            return reverse_lazy('employee_dashboard')
        return reverse_lazy('login')
    

@method_decorator(csrf_protect, name="dispatch")
class CustomLogoutView(View):
    @method_decorator(require_POST)
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect("login")
    

class AdminSignupView(CreateView):
    form_class = AdminSignUpForm
    template_name = 'registration/signup_form.html'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Admin'
        return super().get_context_data(**kwargs)
    
    def get_success_url(self):
        return reverse_lazy('login')  


class TechnicianSignupView(CreateView):
    form_class = TechnicanSignUpForm
    template_name = 'registration/signup_form.html'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Technician'
        return super().get_context_data(**kwargs)
    
    def get_success_url(self):
        return reverse_lazy('login')  


class EmployeeSignUpView(CreateView):
    form_class = EmployeeSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Employee'
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        return reverse_lazy('login')  


@require_POST
def demo_login(request):
    username = os.environ.get("DEMO_USERNAME", "demo")
    password = os.environ.get("DEMO_PASSWORD")

    if not password:
        return redirect("login")

    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)

       
        if getattr(user, "is_admin", False):
            return redirect("admin_dashboard")
        elif getattr(user, "is_technician", False):
            return redirect("technician_dashboard")
        elif getattr(user, "is_employee", False):
            return redirect("employee_dashboard")

        return redirect("home")

    
    return redirect("login")