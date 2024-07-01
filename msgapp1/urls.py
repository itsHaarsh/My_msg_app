from django.urls import path
from message_app import views

urlpatterns = [
    path('testing', views.testing),
    path('create', views.create),
    path('',views.dashboard),
    path('delete/<rid>',views.delete),
    path('edit/<rid>',views.delete),
    
    
]