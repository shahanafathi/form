"""
URL configuration for pjt1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/',admin.site.urls),
    path('sr',views.sr),
    path('odd/<int:num>',views.odd),
    path('str/<n>',views.str),
    path('abc/<int:n>/<int:m>',views.abc),
    path('',views.index),
    path('ind',views.ind,name='ind'),
    path('vowel/<str:v>',views.vowel),
    path('indo',views.indo,name='indo'),
    path('ind_4',views.ind_4,name='ind_4'),
    path('rgr',views.rgr,name='rgr'),
    path('search',views.search,name='search'),
    path('deleteschool/<int:id>',views.deleteschool,name='deleteschool'),
    path('editschool/<int:id>',views.editschool,name='editschool'),
    
    
]
if settings.DEBUG:
    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
