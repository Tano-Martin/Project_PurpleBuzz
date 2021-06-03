from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.


@admin.register(models.Website)
class WebsiteAdmin(admin.ModelAdmin):
	list_display = ('images_view_a', 'images_view_c', 'images_view_w', 'images_view_ch', 'name', 'phone', 'email', 'copyrights', 'contactTitle', 'contactClientTitle', 'workTitle', 'workDetailTitle', 'workFeaturedTitle', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_editable = ['status']

	def images_view_a(self, obj):
		return mark_safe(f'<img src="{obj.aboutPicture.url}" style="height:100px; width:150px">')
	images_view_a.short_description = 'Apercu des images about'
	
	def images_view_c(self, obj):
		return mark_safe(f'<img src="{obj.contactPicture.url}" style="height:100px; width:150px">')
	images_view_c.short_description = 'Apercu des images contact'

	def images_view_ch(self, obj):
		return mark_safe(f'<img src="{obj.choicePicture.url}" style="height:100px; width:150px">')
	images_view_ch.short_description = 'Apercu des images choice'

	def images_view_w(self, obj):
		return mark_safe(f'<img src="{obj.workPicture.url}" style="height:100px; width:150px">')
	images_view_ch.short_description = 'Apercu des images work'


@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
	list_display = ('images_view', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_editable = ['status']

	def images_view(self, obj):
		return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
	images_view.short_description = 'Apercu des images'

@admin.register(models.Slider)
class SliderAdmin(admin.ModelAdmin):
	list_display = ('title', 'underline', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_editable = ['status']

@admin.register(models.Partner)
class PartnerAdmin(admin.ModelAdmin):
	list_display = ('name', 'icon', 'link', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_editable = ['status']

@admin.register(models.Socialicon)
class SocialiconAdmin(admin.ModelAdmin):
	list_display = ('name', 'icon', 'link', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_editable = ['status']

@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
	list_display = ('images_view', 'name', 'poste', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_editable = ['status']

	def images_view(self, obj):
		return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
	images_view.short_description = 'Apercu des images'

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'phone', 'company', 'subject', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_editable = ['status']

@admin.register(models.Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
	list_display = ('email', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_editable = ['status']

@admin.register(models.Progress)
class ProgressAdmin(admin.ModelAdmin):
	list_display = ('name', 'proportion', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_editable = ['status']

@admin.register(models.Aim)
class AimAdmin(admin.ModelAdmin):
	list_display = ('name', 'icon', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_editable = ['status']
