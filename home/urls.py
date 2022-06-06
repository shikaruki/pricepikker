from django.contrib import admin
from django.urls import path
from  home import views

urlpatterns = [
    path('',views.index,name="home"),
    path('contact',views.contact,name="contact"),
    path('feedback',views.feedback,name="feedback"),
    path("login",views.login,name="login"),
    path("searchProduct",views.search,name="products"),
    path('result',views.result,name="searchedresult"),

]