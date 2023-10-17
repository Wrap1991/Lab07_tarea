from django.contrib import admin

# Register your models here.
from .models import Eventos
from .models import Usuario
admin.site.register(Eventos)
admin.site.register(Usuario)

