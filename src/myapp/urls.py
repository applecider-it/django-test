"""
URL configuration for myapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

from home import views as home_views
from tweet import views as tweet_views
from account import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', home_views.home_view, name='home'),
    path('development/', home_views.development_view, name='development'),

    path('login/', account_views.login_view, name='login'),
    path('logout/', account_views.logout_view, name='logout'),

    path('tweet/', tweet_views.tweet_view, name='tweet'),
]
