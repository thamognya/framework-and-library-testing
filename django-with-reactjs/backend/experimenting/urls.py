from django.urls import path
from . import views
from django.views.generic import TemplateView

# url conf
urlpatterns = [
    path('', views.index, name='index'),
    path('<wildcardurl>', views.wildcard, name='wildcard'),
]