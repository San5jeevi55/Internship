from django.urls import path
from . import views
urlpatterns =[
    
    path("login/",views.login,name="login"),
    path('faculty/', views.faculty, name='faculty'),
    path('get_internship_details/', views.get_internship_details, name='get_internship_details'),
    path('get_internship_response_details/', views.get_internship_response_details, name='get_internship_details'),
    path('student/', views.student, name='student'),
    path('student_page/<int:student_id>/', views.student_page, name='student_page'),
    path('internship/', views.internship_statistics, name='internship'),
    path('dummy/', views.dummy, name='dummy'),
    path('student_internships/', views.student_internships, name='student_internships'),
    path('odrequest/',views.odrequest, name='odrequest'),
    path('approve/',views.approve, name='approve'),
    path('make_announcement/', views.make_announcement, name='make_announcement'),
    path('announcements/', views.announcements, name='announcements')
]