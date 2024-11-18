from django.contrib import admin
from .models import Register,Course,Login

admin.site.register(Register),
admin.site.register(Course),
admin.site.register(Login)