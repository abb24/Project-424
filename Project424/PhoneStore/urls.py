from django.urls import path
from . import views

app_name = 'PhoneStore'
urlpatterns = [
    path("", views.index , name="index"),
    path("add", views.add , name='add'),
    path('products' , views.phone, name='phone_list'),
    path('logina' , views.logina , name='login'),
    path('register', views.register,name="register")

]