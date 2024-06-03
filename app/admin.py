from django.contrib import admin
from . import models


admin.site.register(models.chat)
# Register your models here.

@admin.register(models.Group)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('name',)

