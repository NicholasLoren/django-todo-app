from django.shortcuts import get_object_or_404, render,get_list_or_404
from .models import Todo
from .forms import TodoForm


# Create your views here.
def index(request): 
    todos = get_list_or_404(Todo)
    return render(request,"todos/home.html",{'todos':todos})


def create(request):
    target_url = "todos:create"
    edit = False
    if request.method == "POST":
        form = TodoForm(request.POST) 
        if not form.is_valid():
            return render(request,"todos/create.html",{'form':form,'target_url':target_url,'edit':edit})
        
        form.save() 
        return render(request, "todos/create.html", {'success': "Todo created successfully"})
    else:
        form = TodoForm()
        return render(request, "todos/create.html", {'form': form})
    
def edit(request,todo_id):
    todo = get_object_or_404(Todo,pk=todo_id) 
    
    if request.method == "POST":
        form = TodoForm(request.POST,instance=todo)
        if not form.is_valid():
            return render(request, "todos/create.html", {'form': form})

        form.save()
        return render(request, "todos/create.html", {'success': "Todo updated successfully"})
    else:
        form = TodoForm(instance=todo)
        return render(request, "todos/create.html", {'form':form,'todo':todo}) 
    

def delete (request,todo_id):
    todo = get_object_or_404(Todo,pk=todo_id)
    todo.delete()
 
    return render(request,"todos/delete.html")   

