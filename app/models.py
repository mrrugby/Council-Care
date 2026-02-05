from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_technician = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

class Employee(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class Technician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
   
    def __str__(self):
        return self.user.username

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  
    def __str__(self):
        return self.user.username
   

class RepairRequest(models.Model):

   STATUS_CHOICES = [
       ('PENDING', 'Pending'),
       ('IN_PROGRESS', 'In Progress'),
       ('COMPLETED', 'Completed'),
       ('REJECTED', 'Rejected')
   ]
   
   employee = models.ForeignKey(Employee, on_delete=models.CASCADE, )
   technician = models.ForeignKey(Technician, on_delete=models.SET_NULL, null=True, blank=True, related_name='requests')
   description = models.TextField()
   status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   
   
   image = models.ImageField(upload_to='repair_requests/', null=True, blank=True)
   def __str__(self):
    return f"Request #{self.id} by {self.employee.user.username}"
 

class RepairRequestComment(models.Model):
    repair_request = models.ForeignKey(RepairRequest, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.user.username} on Request #{self.repair_request.id}"

    
    
class StatusHistory(models.Model):
    repair_request = models.ForeignKey(RepairRequest, on_delete=models.CASCADE,)
    status = models.CharField(max_length=20, choices=RepairRequest.STATUS_CHOICES)
    updated_at= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Request #{self.repair_request.id} updated to {self.status}"
