from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def layout_static(request):
    return render(request, 'layout-static.html')

def layout_sidenav_light(request):
    return render(request, 'layout-sidenav-light.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def password(request):
    return render(request, 'password.html')

def e401(request):
    return render(request, '401.html')

def e404(request):
    return render(request, '404.html')

def e500(request):
    return render(request, '500.html')

def charts(request):
    return render(request, 'charts.html')

def tables(request):
    return render(request, 'tables.html')