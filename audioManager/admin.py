from django.contrib import admin
from .models import dropboxToken, Song

admin.site.register(dropboxToken)
admin.site.register(Song)
# Register your models here.
