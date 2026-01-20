from django.urls import path
from . import views

app_name = 'folio'

urlpatterns = [
    path('folio', views.home, name='home'),
    path('', views.folio, name='folio'),
    path('test', views.test, name='test'),
    path('message/api', views.message, name='message')
]