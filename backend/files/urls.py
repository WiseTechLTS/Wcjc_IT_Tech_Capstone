from django.urls import path, include
from files import views

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

urlpatterns = [
    path('', views.user_files),
    path('all/', views.get_all_files),
]
