from django.shortcuts import render
from .models import Category,Photo
# Create your views here.

def gallery(request):
    category=request.GET.get('category')
    if category == None:
        photos=Photo.objects.all()
    else:
        photos=Photo.objects.filter(category__name__contains=category)


    categories=Category.objects.all()
    

    context={'categories':categories,'photos': photos}
    return render(request,'photos/gallery.html',context)

def viewPhoto(request,pk):
    photo=Photo.objects.get(id=pk)
    return render(request,'photos/photo.html', {'photo':photo})

def addPhoto(request):
    return render(request,'photos/add.html')