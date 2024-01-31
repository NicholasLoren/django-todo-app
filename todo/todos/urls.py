from django.urls import path 
from . import views


app_name = "todos"

urlpatterns = [
    path('',views.index,name="home"),
    path('create',views.create,name="create"),
    path('edit/<int:todo_id>',views.edit,name="edit"), 
    path('delete/<int:todo_id>',views.delete,name="delete"), 
]
