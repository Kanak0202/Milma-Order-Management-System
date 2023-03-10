"""signin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from . import views
from signup import views1
from mshop import views
from madmin import viewsAdmin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index, name="index"),
    path("signupm/",views1.signup, name="signup"),
    path("login/",views1.Login, name="login"),
    path("logout/",views1.handleLogout, name="logout"),
    path("next/",views1.next, name="next"),
    path('mshop/', include('mshop.urls'), name="mshop"),
    path('madmin/', include('madmin.urls'), name="madmin"),
    path('currentOrder/', viewsAdmin.currentOrder, name="currentOrder"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
