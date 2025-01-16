from django.urls import path
from. import views


app_name="home"

urlpatterns = [  
    path('', views.home, name='home'),
    path('login/',views.user_login,name="login"),
    path('aboutus/',views.about_us,name="about_us"),
    path('Shree-Rastriya-Secondary-School/admin',views.admin_panel,name="admin-settings"),
    path('Shree-Rastriya-Secondary-School/admin/event/lists',views.Events_List,name='events'),
]