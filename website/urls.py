from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('pricing/', views.pricing, name="pricing"),
    path('work/', views.work, name="work"),
    path('work-single/<int:id_work>', views.workSingle, name="workSingle"),
    path('newsletterForm/', views.newsletterForm, name="newsletterForm"),
    path('contactForm/', views.contactForm, name="contactForm"),
    
]

if settings.DEBUG :
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
