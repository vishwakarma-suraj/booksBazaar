from django.db import models


class Category(models.Model):
    name=models.CharField(max_length=200,db_index=True)
    
    def __str__(self):
        return self.name
    
    
    
class Book(models.Model):
    name=models.CharField(max_length=200,db_index=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='allbooks')
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name