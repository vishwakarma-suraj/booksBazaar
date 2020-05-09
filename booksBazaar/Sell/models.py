from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    img=models.ImageField(blank=True,default='c.jpg')
    description=models.TextField(blank=True)
    contact=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='Sell_posts')
    created = models.DateTimeField(auto_now_add=True)
	
	

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('Sell:post_detail',args=[self.id])
        
        

        
        
    

	