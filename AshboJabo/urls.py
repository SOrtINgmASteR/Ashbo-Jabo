"""
URL configuration for AshboJabo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from Bookings import views as book_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', book_view.home, name="home"),
    path('about_us/', book_view.about_us, name="about_us"),
    path('book/', book_view.book, name="book"),
    path('popular_destination/', book_view.popular_destination, name="popular_destination"),
    path('add_popular_destination/', book_view.add_popular_destination, name="add_popular_destination"),
    path('delete_popular_destination/<str:id>', book_view.delete_popular_destination, name="delete_popular_destination"),
    path('update_popular_destination/<str:id>', book_view.update_popular_destination, name="update_popular_destination"),
    path('log_in/', book_view.log_in, name="log_in"),
    path('sign_up/', book_view.sign_up, name="sign_up"),
    path('logout/', book_view.custom_logout, name='logout'),

]
