from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Movie
from . forms import MovieForm
# Create your views here.
def start(request):
    obj=Movie.objects.all()
    return render(request,'home.html',{'final':obj})

def details(request,movie_id):
    obj1=Movie.objects.get(id=movie_id)
    # return HttpResponse('this is no %s' % movie_id)
    return render(request,'details.html',{'result':obj1})

def add(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        img = request.FILES['img']
        movies=Movie(name=name,desc=desc,year=year,img=img)
        movies.save();
    return render(request,'add.html')

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'movie':movie,'form':form})

def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')

