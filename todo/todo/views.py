from django.shortcuts import render,redirect

def not_found(request, exception):
    return render(request, "404.html", {}, status=404) 

def index(request):
   return redirect("todos:home")






