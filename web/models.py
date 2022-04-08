from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django import forms



RATING_CHOICES = (
    ("3","3"),
    ("3.5","3.5"),
    ("4","4"),
    ("4.5","4.5"),
    ("5","5")
    
)


class Users(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	country = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	apartment = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=255)
	pincode = models.CharField(max_length=255)
	phone = models.CharField(max_length=255, blank=True)
	email = models.CharField(max_length=255, blank=True,default="test@gmail.com")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	
	class Meta:
		db_table = 'Users'
		ordering = ['-created_at']
	
	def __str__(self):
		return(self.first_name +" "+ self.last_name)


class Product(models.Model):
	name = models.CharField(max_length=255)
	description = RichTextField()
	bannerImage = models.URLField(max_length=255, blank=True)
	offer_price = models.FloatField(default=0)
	actual_price = models.FloatField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	is_best_selling = models.BooleanField(default=False)
	total_num_of_reviews = models.IntegerField(default=243)
	gif_image_url1 = models.URLField(max_length=255, blank=True)
	gif_image_url2 = models.URLField(max_length=255, blank=True)
	gif_image_url3 = models.URLField(max_length=255, blank=True)
	star_value = models.CharField(max_length=128, choices = RATING_CHOICES,default = "5")

	
	class Meta:
		db_table = 'products'
	
	def __str__(self):
		return self.name


class ProductImage(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	image = models.URLField(max_length=255, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	class Meta:
		db_table = 'product_images'
	
	def __str__(self):
		return self.product.name



class ProductReview(models.Model):
	product = models.ForeignKey(Product, on_delete = models.CASCADE)
	name = models.CharField(max_length=255)
	description = models.TextField()
	rating = models.CharField(max_length=128, choices = RATING_CHOICES,default = "5")
	created_at = models.DateTimeField(auto_now_add=True)
	img1 = models.ImageField(upload_to="images/",blank=True)
	img2 = models.ImageField(upload_to="images/",blank=True)
	img3 = models.ImageField(upload_to="images/",blank=True)
	img4 = models.ImageField(upload_to="images/",blank=True)
	img5 = models.ImageField(upload_to="images/",blank=True)
	review_duration = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(12)])
	updated_at = models.DateTimeField(auto_now=True)
	
	class Meta:
		db_table = 'product_reviews'
	def __str__(self):
    		return self.product.name


class OrderItem(models.Model):
	item = models.ForeignKey(Product, on_delete=models.CASCADE)
	user = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	qty = models.IntegerField(default=1)
 
	class Meta:
		db_table = 'orders'
	def __str__(self):
    		return self.item.name


class Message(models.Model):
	name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	phone = models.CharField(max_length=255, blank=True)
	message = models.CharField(max_length=500)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
 
	class Meta:
		db_table = 'messages'
	def __str__(self):
    		return self.name

class NewsLetter(models.Model):
	email = models.CharField(max_length=255)
	
	class Meta:
		db_table = 'news_letter'
	def __str__(self):
    		return self.email