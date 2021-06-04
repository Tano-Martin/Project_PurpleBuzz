from django.db import models
from django.db.models.fields import URLField
from tinymce.models import HTMLField

# Create your models here.
class Service(models.Model):
	name = models.CharField(max_length=255)
	picture = models.FileField(upload_to='Service_file')
	description = models.TextField()
	category = models.ForeignKey('service.Categoryservice', related_name='categoryService', on_delete=models.CASCADE)
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Service'
		verbose_name_plural = 'Services'

	def __str__(self):
		return self.name

class Categoryservice(models.Model):
	name = models.CharField(max_length=255)
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Categoryservice'
		verbose_name_plural = 'Categoryservices'

	def __str__(self):
		return self.name

class Contactservice(models.Model):
	name = models.CharField(max_length=255) 
	postAgent = models.CharField(max_length=255)
	icon = models.CharField(max_length=255)
	phone = models.CharField(max_length=255)
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Contactservice'
		verbose_name_plural = 'Contactservices'

	def __str__(self):
		return self.name

class Pricing(models.Model):
	picture = models.FileField(upload_to='Pricing_file')
	description = models.TextField()
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Pricing'
		verbose_name_plural = 'Pricings'

	def __str__(self):
		return f'{self.picture}'

class Pricingform(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	price = models.IntegerField(default=0)
	period = models.CharField(max_length=255, blank=True)
	active = models.BooleanField(default=False)
	advantage = models.ManyToManyField('service.Advantage', related_name='advantagePricing')
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Pricingform'
		verbose_name_plural = 'Pricingforms'

	def __str__(self):
		return self.name

class Advantage(models.Model):
	name = models.CharField(max_length=255)
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Advantage'
		verbose_name_plural = 'Advantages'

	def __str__(self):
		return self.name

class Categorywork(models.Model):
	name = models.CharField(max_length=255)
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Categorywork'
		verbose_name_plural = 'Categoryworks'

	def __str__(self):
		return self.name

class Work(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	document = HTMLField(blank=True)
	video = models.URLField(blank=True)
	picture = models.FileField(upload_to="work_file")
	category = models.ForeignKey('service.Categorywork', related_name='category_work', on_delete=models.CASCADE)
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Work'
		verbose_name_plural = 'Works'

	def __str__(self):
		return self.title

class Picturework(models.Model):
	picture = models.FileField(upload_to='Picturework_file')
	work = models.ForeignKey('service.Work', related_name='picture_work', on_delete=models.CASCADE)
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Picturework'
		verbose_name_plural = 'Pictureworks'

	def __str__(self):
		return f'{self.picture}'

class Workfeatured(models.Model):
	title = models.CharField(max_length=255)
	picture = models.FileField(upload_to='Workfeatured_file')
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Workfeatured'
		verbose_name_plural = 'Workfeatureds'

	def __str__(self):
		return self.title
