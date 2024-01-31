from django.contrib import admin
from .models import Todo
# Register your models here.

class TodosAdmin(admin.ModelAdmin):
    list_display = ("id","title","description")
    exclude = ("created_at",)



admin.site.register(Todo,TodosAdmin)