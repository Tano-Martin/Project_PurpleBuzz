from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Website(models.Model):
	name = HTMLField()
	phone = models.CharField(max_length=255)
	email = models.EmailField()
	copyrights = models.CharField(max_length=255)
	contactTitle = models.CharField(max_length=255)
	contactDescription = models.TextField()
	contactPicture = models.FileField(upload_to='Website_file')
	contactClientTitle = models.CharField(max_length=255)
	contactClientDescription = models.TextField()
	choicePicture = models.FileField(upload_to='Website_file')
	choiceDescription = models.TextField()
	aboutPicture = models.FileField(upload_to='Website_file')
	aboutDescription = models.TextField()
	workTitle = models.CharField(max_length=255)
	workPicture = models.FileField(upload_to='Website_file')
	workDescription = models.TextField()
	workDetailTitle = models.CharField(max_length=255)
	workDetailDescription = models.TextField()
	workFeaturedTitle = models.CharField(max_length=255)
	workFeaturedDescription = models.TextField()
	descriptionService = models.TextField()
	descriptionTeam = models.TextField()
	descriptionProgress = models.TextField()
	descriptionNewsletter = models.TextField()
	descriptionPricing = models.TextField()
	descriptionFooter = models.TextField()
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Website'
		verbose_name_plural = 'Websites'

	def __str__(self):
		return self.name

class Banner(models.Model):
	picture = models.FileField(upload_to='Banner_file')
	slider = models.ManyToManyField('website.Slider', related_name='bannerSlide')
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Banner'
		verbose_name_plural = 'Banners'

	def __str__(self):
		return f'{self.picture}'

class Slider(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	underline = models.BooleanField(default=False, blank=True)
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Slider'
		verbose_name_plural = 'Sliders'

	def __str__(self):
		return self.title

class Partner(models.Model):
	name = models.CharField(max_length=255)
	icon = models.CharField(max_length=255)
	link = models.URLField()
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Partner'
		verbose_name_plural = 'Partners'

	def __str__(self):
		return self.name

class Socialicon(models.Model):
	name = models.CharField(max_length=255)
	icon = models.CharField(max_length=255)
	link = models.URLField()
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Socialicon'
		verbose_name_plural = 'Socialicons'

	def __str__(self):
		return self.name

class Team(models.Model):
	name = models.CharField(max_length=255)
	poste = models.CharField(max_length=255)
	picture = models.FileField(upload_to='Team_file')
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Team'
		verbose_name_plural = 'Teams'

	def __str__(self):
		return self.name

class Contact(models.Model):
	name = models.CharField(max_length=255)
	email = models.URLField()
	phone = models.CharField(max_length=255)
	company = models.CharField(max_length=255)
	subject = models.CharField(max_length=255)
	message = models.TextField()
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Contact'
		verbose_name_plural = 'Contacts'

	def __str__(self):
		return self.name

class Newsletter(models.Model):
	email = models.EmailField()
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Newsletter'
		verbose_name_plural = 'Newsletters'

	def __str__(self):
		return f'{self.email}'

class Progress(models.Model):
	name = models.CharField(max_length=255)
	proportion = models.IntegerField(default=0)
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Progress'
		verbose_name_plural = 'Progress'

	def __str__(self):
		return self.name

class Aim(models.Model):
	name = models.CharField(max_length=255)
	icon = models.CharField(max_length=255)
	description = models.TextField()
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Aim'
		verbose_name_plural = 'Aims'

	def __str__(self):
		return self.name

