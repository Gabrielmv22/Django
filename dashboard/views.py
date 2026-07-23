from django.shortcuts import render

def base(request):
    # Ahora Python ya sabe qué es 'render'
    return render(request, 'base.html')