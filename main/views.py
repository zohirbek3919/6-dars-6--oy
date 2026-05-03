from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import NewForm
from .models import Category, New


def home(request):
    categories = Category.objects.all()
    news = New.objects.all()
    context = {
        'categories': categories,
        'news': news,
    }
    return render(request, 'main/index.html', context)


def new_detail(request, new_id):
    new = New.objects.get(id=new_id)
    categories = Category.objects.all()
    context = {
        'new': new,
        'categories': categories,
    }
    return render(request, 'main/detail.html', context)


def new_by_categories(request, category_id):
    categories = Category.objects.all()
    category = Category.objects.get(id=category_id)
    news = New.objects.filter(turi=category)

    context = {
        'categories': categories,
        'news': news,
        'type': category.name,
    }
    return render(request, 'main/index.html', context)


def add_new(request: HttpRequest):
    if request.method == 'POST':
        form = NewForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new = form.save()
            return redirect('detail', new_id=new.pk)
    else:
        form = NewForm()

    context = {
        'form': form,
    }
    return render(request, 'main/add_new.html', context)