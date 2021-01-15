"""hyperjob URL Configuration

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
from django.urls import path, re_path
from menu.views import MenuView
from vacancy.views import VacanciesView
from resume.views import ResumesView
from django.views.generic import RedirectView
from auth.views import MyLoginView, MySignupView
from django.contrib.auth.views import LogoutView
from home.views import HomePage

urlpatterns = [
    path('admin', admin.site.urls),
    path('', MenuView.as_view()),
    path('vacancies', VacanciesView.as_view()),
    path("resumes", ResumesView.as_view()),
    path('vacancy/new', VacanciesView.as_view()),
    path("resume/new", ResumesView.as_view()),
    path('login', MyLoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('signup', MySignupView.as_view()),
    path('home', HomePage.as_view()),
    path('home/', RedirectView.as_view(url='/home')),
    path('login/', RedirectView.as_view(url='/login')),
    path('signup/', RedirectView.as_view(url='/signup')),
    path('logout/', RedirectView.as_view(url='/logout')),
    # path('menu/', RedirectView.as_view(url='/'))
    # re_path("(?P<link>[^/]*)/?", CandyView.as_view())
]
