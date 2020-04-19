from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<argument>', views.get_argument, name='get_argument'),
]
