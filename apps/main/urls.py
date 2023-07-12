from django.urls import path, include
from .views import home

app_name = 'main'

urlpatterns = [
    # api based path
    path('api/', include('apps.main.api.urls', namespace='api')),

    # template based views
    path('', home, name='home')
]
