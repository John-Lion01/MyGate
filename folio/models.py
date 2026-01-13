from django.db import models
from parler.models import TranslatableModel, TranslatedFields

# Create your models here.
class Config(TranslatableModel) :
    translation = TranslatedFields(
        home_description = models.TextField(),
    )
    name = models.CharField(max_length=50)

    logo = models.ImageField(upload_to='folio/config', blank=True, name='logo')
    main_image = models.ImageField(upload_to='folio/config', blank=True, name='main_image')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)