# Sending email from google smpt:

**1. SMTM config in `setings.py` (put your email credentials in your `.env` file )**
```
...
# GOOGLE SMTP
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
```

**2. Sending mail function in your views (not required!)** 

```
from django.conf import settings
from django.core.mail import send_mail
...


def your_view(request):
    ...
    send_mail(subject='Message subject!', 
              message='Message body...', 
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=['******@***.***'])
    ...
    return ...
```
