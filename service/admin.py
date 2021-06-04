from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.

@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
	list_display = ('images_view', 'name', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_editable = ['status']

	def images_view(self, obj):
		return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
	images_view.short_description = 'Apercu des images'

@admin.register(models.Categoryservice)
class CategoryserviceAdmin(admin.ModelAdmin):
	list_display = ('name', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_editable = ['status']

@admin.register(models.Contactservice)
class ContactserviceAdmin(admin.ModelAdmin):
	list_display = ('name', 'postAgent', 'icon', 'phone', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_editable = ['status']

@admin.register(models.Pricing)
class PricingAdmin(admin.ModelAdmin):
	list_display = ('images_view', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_editable = ['status']

	def images_view(self, obj):
		return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
	images_view.short_description = 'Apercu des images'

@admin.register(models.Pricingform)
class PricingformAdmin(admin.ModelAdmin):
	list_display = ('name', 'price', 'period', 'active', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_editable = ['status']

@admin.register(models.Advantage)
class AdvantageAdmin(admin.ModelAdmin):
	list_display = ('name', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_editable = ['status']

@admin.register(models.Categorywork)
class CategoryworkAdmin(admin.ModelAdmin):
	list_display = ('name', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_editable = ['status']

@admin.register(models.Work)
class WorkAdmin(admin.ModelAdmin):
	list_display = ('images_view', 'title', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_editable = ['status']

	def images_view(self, obj):
		return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
	images_view.short_description = 'Apercu des images'

@admin.register(models.Picturework)
class PictureworkAdmin(admin.ModelAdmin):
	list_display = ('images_view', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_editable = ['status']

	def images_view(self, obj):
		return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
	images_view.short_description = 'Apercu des images'

@admin.register(models.Workfeatured)
class WorkfeaturedAdmin(admin.ModelAdmin):
	list_display = ('images_view', 'title', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_editable = ['status']

	def images_view(self, obj):
		return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
	images_view.short_description = 'Apercu des images'
