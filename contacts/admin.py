from django.contrib import admin
from .models import *


class SupportAdmin(admin.ModelAdmin):
    save_as = True
    fields = [('email', 'name', 'phone'), 'subject', 'message', ('created', 'updated')]
    list_display = ['name', 'email', 'phone', 'Тема', 'Сообщение', 'created']
    list_filter = ['email']
    search_fields = ['email', 'name', 'phone']

    class Meta:
        model = Support


admin.site.register(Support, SupportAdmin)
