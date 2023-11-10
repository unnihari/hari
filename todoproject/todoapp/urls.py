from django.contrib import admin
from django.urls import path, include

from todoapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:taskid>',views.delete,name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('cbuhome/',views.TaskListview.as_view(),name='cbuhome'),
    path('cbudetails/<int:pk>/',views.TaskDetailView.as_view(),name='cbudetails'),
    path('cbuupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='cbuupdate'),
    path('cbudelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cbudelete'),
]
