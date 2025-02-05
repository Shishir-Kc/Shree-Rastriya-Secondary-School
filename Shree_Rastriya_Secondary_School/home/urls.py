from django.urls import path
from. import views


app_name="home"

urlpatterns = [  
    path('', views.home, name='home'),
    path('accounts/login/',views.user_login,name="login"),
    path('Shree-Rastriya-Secondary-School/login/',views.user_login,name="login"),
    path('about-us/',views.about_us,name="about_us"),
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
    path('Shree-Rastriya-Secondary-School/teacher/',views.teacher_manage,name='teacher'),
    path('Shree-Rastriya-Secondary-School/administrator/',views.Administrator,name='ah'),
    # path('Shree-Rastriya-Secondary-School/Eduaction/',views.scholarship_and_fees,name='Edu'),
    path('Shree-Rastriya-Secondary-School/admin/teacher/manage',views.manage_teacher,name='teacher-manage'),
    path('Shree-Rastriya-Secondary-School/admin/teacher/manage/delete/<int:teacher_id>/',views.delete_teacher,name='teacher-delete'),
    path('Shree-Rastriya-Secondary-School/admin/teacher/manage/edit/<int:teacher_id>/',views.Edit_teacher,name='edit-teacher'),
    path('Shree-Rastriya-Secondary-School/gallery/',views.Gallery,name='gallery'),
    path('Shree-Rastriya-Secondary-School/gallery/list',views.list_gallery,name='list-gallery'),    
    path('Shree-Rastriya-Secondary-School/gallery/add/',views.add_gallery,name='add-gallery'),   
    path('Shree-Rastriya-Secondary-School/gallery/list/edit/<int:photo_id>/',views.Edit_photo,name='edit-gallery'),  
    path('Shree-Rastriya-Secondary-School/gallery/list/edit/delete/<int:photo_id>/',views.Del_Photo,name='del-gallery'),  
    path('Shree-Rastriya-Secondary-School/contact/',views.Contact,name='contact'),
    path('Shree-Rastriya-Secondary-School/contact/list/',views.contact_list,name='contact-list'),
    path('Shree-Rastriya-Secondary-School/contact/list/<int:contact_id>/',views.contact_detail,name='contact-detail'),
    path('Shree-Rastriya-Secondary-School/contact/list/<int:contact_id>/delete/',views.Delete_contact,name='delete-contact'),
    path('Shree-Rastriya-Secondary-School/administrator/add/',views.add_Administrator,name="add-administrator"),
    path('Shree-Rastriya-Secondary-School/administrator/edit/<int:administrator_id>/',views. Detail_administrator,name="detail-administrator"),
    path('Shree-Rastriya-Secondary-School/administrator/delete/<int:admin_id>/',views.Delete_administrator,name="delete-administrator"),
    path('Shree-Rastriya-Secondary-School/Notice/',views.Notice,name='notice'),
    path('Shree-Rastriya-Secondary-School/Notice/<int:notice_id>/',views.Notice_id,name='notice-view'),
    path('Shree-Rastriya-Secondary-School/Notice/add',views.Add_Notice,name='add-notice'),
    path('Shree-Rastriya-Secondary-School/Education/',views.Scholar_FeeStructure,name='edu'),
    # path('Shree-Rastriya-Secondary-School/Education/admin/',views.edit_Scholar,name='list-scholar'),
    # path('Shree-Rastriya-Secondary-School/Education/admin/<int:scholar_id>/',views.edit_Scholar,name='edit-scholar'),


    #  ~ ~ below here are the test urls ! ~ ~ ~ 
    path('Shree-Rastriya-Secondary-School/Notice/<int:notice_id>/delete/',views.notice_delete,name='notice-delete'),
   # ~ ~ ~ remove this path after testing ~ ~ ~ 
    path('test/',views.test,name='test'),
   #
    path('std/<int:std_id>/',views.student_profile,name="profile"),
    path('std/',views.student_list,name="std-list"),
    path('upload/',views.upload_notes,name='upload'),
    path('dashboard/', views.student_dashboard, name='student_dashboard'),
    path('teacher/',views.teacher_list, name='teacher-list'),
    path('teacher/chat/<int:teacher_id>/',views.teacher_chat, name='teacher-chat'),
    path('settings/',views.student_settings, name='student_settings'),
    path('books/',views.Student_Books,name='student_books'),
    path('student/',views.student_profile,name='student_profile'),
 
]  