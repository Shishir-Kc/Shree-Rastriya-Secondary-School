from django.urls import path
from. import views


app_name="home"

urlpatterns = [  
    path('', views.home, name='home'),
    path('Shree-Rastriya-Secondary-School/login/',views.user_login,name="login"),
    path('aboutus/',views.about_us,name="about_us"),
    path('Shree-Rastriya-Secondary-School/admin',views.admin_panel,name="admin-settings"),
    path('Shree-Rastriya-Secondary-School/admin/event/lists',views.Events_List,name='events'),
    path('Shree-Rastriya-Secondary-School/log-out/',views.user_logout,name="logout"),
    path('Shree-Rastriya-Secondary-School/admin/event/list/<int:event_id>',views.Event_updater,name="update_event"),
    path('Shree-Rastriya-Secondary-School/admin/event/list/<int:event_id>/delete',views.Delete_Event,name="Delete_event"),
    path('Shree-Rastriya-Secondary-School/admin/event/list/add',views.Event_add,name="add_event"),
    path('Shree-Rastriya-Secondary-School/admin/event/add',views.Event_add,name="add_event"),
    path('Shree-Rastriya-Secondary-School/admin/staff/manage',views.staff_list,name='staff-manage'),
    path('fail-safe/<int:user_id>/',views.fail_safe,name='safe'),
     path('Shree-Rastriya-Secondary-School/admin/staff/manage/delete/<int:staff_id>',views.staff_delete,name='staff-delete'),

    
]   