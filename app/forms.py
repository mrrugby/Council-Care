from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth.forms import AuthenticationForm
from app.models import Admin, Employee, RepairRequest,Technician, StatusHistory, User, RepairRequestComment


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        labels = {
            'username' : 'Username',
            'password1' : 'Password',
            'password2' : 'Confirm Password',
        }
        help_texts = {
            'username' : None,
            'password1' : None,
            'password2' :None
        }
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username',
        })
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter a secure password',
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm your password',
        })
        



class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class' : 'form-control', 'placeholder' : 'Username'})
        self.fields['password'].widget.attrs.update({'class' : 'form-control', 'placeholder' : 'Password'})
        
class EmployeeSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_employee = True
        if commit:
            user.save()
            Employee.objects.create(user=user)
        return user
        
        
        
class TechnicanSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_technician = True
        if commit:
            user.save()
            Technician.objects.create(user=user)
        return user
    
    
class AdminSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        
    @transaction.atomic
    def save(self,commit=True):
        user = super().save(commit=False)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        if commit:
            user.save()
            Admin.objects.create(user=user)
        return user


# Employee Repair Requests
class RepairRequestForm(forms.ModelForm):
    class Meta:
        model = RepairRequest
        fields = ['description', 'image']
        widgets = {
            'description' : forms.Textarea(attrs={'placeholder':'Describe the issue...', 'rows':4}),
        }
        
        
# Technician Update Repair Status
class UpdateStatusForm(forms.ModelForm):
    class Meta:
        model = RepairRequest
        fields = ['status']
        widgets = {
            'status' : forms.Select(choices=RepairRequest.STATUS_CHOICES),
        }

class StatusHistoryForm(forms.ModelForm):
    class Meta:
        model = StatusHistory
        fields = ['status']
        widgets = {
            'status' : forms.Select(choices=RepairRequest.STATUS_CHOICES),
        }

class RepairRequestCommentForm(forms.ModelForm):
    class Meta:
        model = RepairRequestComment
        fields = ['comment']