from django.shortcuts import render
from .models import Servic, kada, Contact
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings

def index(request):

    service = Servic.objects.filter()[:3]
    service1 = Servic.objects.filter()[3:6]
    service2 = Servic.objects.filter()[6:]
    details = kada.objects.all()

    if request.method == 'POST':
        contact = Contact()
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message')
        contact.fullname = fullname
        contact.email = email
        contact.number = number
        contact.message = message
        contact.save()

        send_mail(fullname, message,settings.EMAIL_HOST_USER,[email],fail_silently=False)

        return HttpResponse("Thanks for contacting us. We will contact you as soon as possible.")

    return render(request, 'index.html', {'service': service, 'service1': service1, 'service2': service2, 'details': details })
