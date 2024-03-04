
from . import views
from django.urls import path
app_name='movieapp'
urlpatterns = [
    path('',views.start,name='start'),
    path('movie/<int:movie_id>/',views.details,name='details'),
    path('add/',views.add,name='add'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('add/',views.add,name='add'),


]