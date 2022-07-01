from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path

# urlpatterns = [
#     path('polls/',('playground.urls')),
#     path('admin/', admin.site.urls),
# ]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
