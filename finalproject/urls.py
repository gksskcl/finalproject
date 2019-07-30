"""finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import final.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', final.views.home, name="home"),
    path('final/Europe',final.views.Europe, name="Europe"),
    path('final/Africa',final.views.Africa, name="Africa"),
    path('final/Australia',final.views.Australia, name="Australia"),
    path('final/South_America',final.views.South_America, name="South_America"),
    path('final/North_America',final.views.North_America, name="North_America"),
    path('final/new',final.views.new, name="new"),
    path('final/new1',final.views.new1, name="new1"),
    path('final/new2',final.views.new2, name="new2"),
    path('final/new3',final.views.new3, name="new3"),
    path('final/new4',final.views.new4, name="new4"),
    path('fianl/create',final.views.create, name="create"),
    path('fianl/create1',final.views.create1, name="create1"),
    path('fianl/create2',final.views.create2, name="create2"),
    path('fianl/create3',final.views.create3, name="create3"),
    path('fianl/create4',final.views.create4, name="create4"),
]
