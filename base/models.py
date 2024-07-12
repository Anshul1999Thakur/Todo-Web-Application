from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    Priority = (('Low','low'),
    ('Medium','Medium'),
    ('High', 'High'))
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=200)
    discription = models.TextField(null=True,blank=True)
    due_date =models.DateField(default=None, null=True, blank=True) 
    priority = models.CharField(max_length=10,choices=Priority, default='L')
    complete = models.BooleanField(default=False)
    # created = models.DateTimeField(auto_now_add=True)
  
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']