from django.urls import path
from .views import folio

app_name = 'folio'

urlpatterns = [
    path('', folio, name='folio')
]