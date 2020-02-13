from django.db import models
from django.urls import reverse

class Category(models.Model):
	name=models.CharField(max_length=200,db_index=True)
	slug = models.SlugField(max_length=200,unique=True)
	def __str__(self):
		return self.name
    
	def get_absolute_url(self):
		return reverse('app1:book_list_by_category',args=[self.slug])
    
class Book(models.Model):
	name=models.CharField(max_length=200,db_index=True)
	slug = models.SlugField(max_length=200, db_index=True)
	category=models.ForeignKey(Category,on_delete=models.CASCADE)
	image=models.ImageField()
	description=models.TextField(blank=True)
	price=models.DecimalField(max_digits=10,decimal_places=2)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	
	class Meta:
		ordering = ('name',)
		index_together = (('id', 'slug'),)
    
	def __str__(self):
		return self.name
		
	def get_absolute_url(self):
		return reverse('app1:book_detail',args=[self.id, self.slug])