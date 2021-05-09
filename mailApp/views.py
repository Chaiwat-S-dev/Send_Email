from django.shortcuts import render, redirect
from django.core.mail import send_mail

# Create your views here.
def sendEmail(request):

    if request.method == 'POST':
        data = {
            'name': request.POST.get('FullName'),
            'email': request.POST.get('Email'),
            'subject': request.POST.get('Subject'),
            'content': request.POST.get('Content')
        }
        
        # String Format content in email
        message = '''
        Dear: {}

        message: {}
        '''.format(data['name'], data['content'])
        
        send_mail(data['subject'], message, '', [data['email']])

    return render(request, 'index.html')