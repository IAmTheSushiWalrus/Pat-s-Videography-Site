from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.core.mail import EmailMessage


def home(request):

    context = {}

    return render(request, 'vindex.html', context)

def contact(request):
    if request.POST:
        name    = request.POST['name']
        email   = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        full_message = "New Email From %s =  Name: %s  \n Subject: %s \n Message: %s" %(email, name, subject, message)

        to_send = EmailMessage(subject, full_message, to=['donalpatrickosullivan@gmail.com'])
        to_send.send()

        messages.success(request, 'Thanks for reaching out!')

        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
