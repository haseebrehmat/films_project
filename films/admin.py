from django.contrib import admin
from .models import Film, Genre, Director

# Register your models here.
admin.site.register([Director, Film, Genre])
