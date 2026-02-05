from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from app.views.auth import CustomLoginView, CustomLogoutView
from app.views.home import home


from .views.admin_views import (AdminSignUpView, admin_dashboard,  view_request_details, update_request_status,)


from .views.technician_views import (
    TechnicianSignUpView,
    technician_dashboard, update_task_status,
)

from .views.employee_views import (
    EmployeeSignUpView, employee_dashboard, create_repair_request, view_repair_request,
)

urlpatterns = [
    #auth
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    
    #home
    path('', home, name='home'), 
    
    #admin
    path('admin/signup/', AdminSignUpView.as_view(), name='admin_signup'),
    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),
    path('admin/request/<int:request_id>/', view_request_details, name='view_request_details'),
    path('admin/request/<int:request_id>/update/', update_request_status, name='update_request_status'),
    
    #tech
    path('technician/signup/', TechnicianSignUpView.as_view(), name='technican_signup'),
    path('technician/dashboard/', technician_dashboard, name='technician_dashboard'),
    path('technician/request/<int:request_id>/update/<str:employee_username>/', update_task_status, name='update_task_status'),
    
    # Employee 
    path('employee/signup/', EmployeeSignUpView.as_view(), name='employee_signup'),
    path('employee/dashboard/', employee_dashboard, name='employee_dashboard'),
    path('employee/request/new/', create_repair_request, name='create_repair_request'),
    path('employee/request/<int:request_id>/', view_repair_request, name='view_repair_request')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)