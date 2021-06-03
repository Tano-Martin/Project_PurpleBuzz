from django.shortcuts import redirect, render
from . import models
from service import models as models_service
from .forms import ContactForm, NewsletterForm

# Create your views here.
def index(request):
    website = models.Website.objects.filter(status=True).first
    socialicons = models.Socialicon.objects.filter(status=True)
    banner = models.Banner.objects.filter(status=True).first
    services = models_service.Service.objects.filter(status=True)
    categoryservice = models_service.Categoryservice.objects.filter(status=True)
    recentworks = models_service.Work.objects.order_by('-date_add')[:6]
    return render(request, "index.html", locals())

def about(request):
    website = models.Website.objects.filter(status=True).first
    socialicons = models.Socialicon.objects.filter(status=True)
    teams = models.Team.objects.filter(status=True)
    partners = models.Partner.objects.filter(status=True)
    progress = models.Progress.objects.filter(status=True)
    aims = models.Aim.objects.filter(status=True)
    return render(request, "about.html", locals())

def contact(request):
    website = models.Website.objects.filter(status=True).first
    socialicons = models.Socialicon.objects.filter(status=True)
    contactServices = models_service.Contactservice.objects.filter(status=True)
    return render(request, "contact.html", locals())

def pricing(request):
    website = models.Website.objects.filter(status=True).first
    socialicons = models.Socialicon.objects.filter(status=True)
    pricingform = models_service.Pricingform.objects.filter(status=True)
    pricing = models_service.Pricing.objects.filter(status=True).first
    advantages = models_service.Advantage.objects.filter(status=True)
    return render(request, "pricing.html", locals())

def work(request):
    website = models.Website.objects.filter(status=True).first
    socialicons = models.Socialicon.objects.filter(status=True)
    works = models_service.Work.objects.filter(status=True)
    news = models_service.Work.objects.order_by('-date_add')[:4]
    categoryworks = models_service.Categorywork.objects.filter(status=True)
    return render(request, "work.html", locals())

def workSingle(request, id_work):
    website = models.Website.objects.filter(status=True).first
    socialicons = models.Socialicon.objects.filter(status=True)
    work = models_service.Work.objects.get(id=id_work)
    workpictures = models_service.Work.objects.filter(status=True)
    return render(request, "work-single.html", locals())

def newsletterForm(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = NewsletterForm()
    return redirect('about')

def contactForm(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ContactForm()
    return redirect('contact')