from django.shortcuts import render, get_object_or_404
from .models import Store, Bookmark, Review, Comment

# Create your views here.

def main(request):
    stores = Store.objects.all()
    query = request.GET.get('query')
    if query:
        stores = Store.objects.filter(title__icontains=query)
        return render(request, 'main.html', {'stores':stores, 'length':len(stores)})

    return render(request, 'main.html', {'stores':stores})

def detail(request, id):
    store = get_object_or_404(Store, pk = id)
    return render(request, 'detail.html', {'store': store})