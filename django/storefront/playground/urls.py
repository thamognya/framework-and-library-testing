from django.urls import path
from . import views

# url conf
urlpatterns = [
    path('', views.index, name='index'),
    path('<word_to_say>', views.wildcard, name='wildcard'),
]