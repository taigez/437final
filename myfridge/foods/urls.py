from django.urls import path, re_path

from . import views

urlpatterns = [
    path('myfood/', views.myfood, name='myfood'),
    path('delete_item/<int:id>/', views.delete_item, name='delete_item'),
    path('scan/', views.scan, name='scan'),
    #re_path(r'^receive_json/$', views.handle_get, name='receive'),
    path('receive_json/', views.handle_post, name='receive'),
]