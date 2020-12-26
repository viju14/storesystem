from django.db import models
from django.contrib.auth.models import User


# Create your models here.

catagore_choice=(
    ('Home appliences','Home appliences'),
    ('IT resources ','IT resources'),
    ('Phone','Phone'),
    ('Electronics','Electronics')

)



class Category(models.Model):
    name=models.CharField(max_length=50 ,blank=True,null=True)
    def __str__(self):
        return self.name

class Stock(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True)
    item_name = models.CharField(max_length=50, null=True, blank=True)
    quantity = models.IntegerField(default='0', null=True, blank=True)
    receive_quantity = models.IntegerField(default='0', null=True, blank=True)
    receive_by = models.CharField(max_length=50, null=True, blank=True)
    issue_quantity = models.IntegerField(default='0', null=True, blank=True)
    issue_by = models.CharField(max_length=50, null=True, blank=True)
    issue_to = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    created_by = models.CharField(max_length=50, null=True, blank=True)
    reorder_level = models.IntegerField(default='0', null=True, blank=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    time_stamp = models.DateTimeField(auto_now_add=True, auto_now=False)



    def __str__(self):
        return str(self.item_name)+" "+str(self.quantity)

