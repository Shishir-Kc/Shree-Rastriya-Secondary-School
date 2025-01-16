from django.urls import path
from. import views


app_name="home"

urlpatterns = [  
    path('', views.home, name='home'),
    path('login/',views.user_login,name="login"),
    path('aboutus/',views.about_us,name="about_us")
]