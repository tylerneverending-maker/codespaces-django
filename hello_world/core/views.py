from django.shortcuts import render


def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)

def development_services(request):
    return render(request, "development_services.html")

def featured_products(request):
    return render(request, "featured_products.html")
