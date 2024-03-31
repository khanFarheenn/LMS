from django.urls import path
from . import views

urlpatterns = [
    path('',views.hello),
    path('getstudent/',views.Studentfun, name='Student'),
    path('getReturn_records/',views.Return_recordsfun, name='Return_records'),
    path('getbook/',views.Booksfun, name='Books'),
    path('getissue/',views.Issuesfun, name='Issue'),
    path('getissue/<int:pk>/',views.Issuesfun, name='Issue'),
    path('getManager/',views.Managerfun, name='Manager'),
    path('getManager/<int:pk>/',views.Managerfun, name='Manager'),
    path('login/',views.loginfun, name='login'),
    path('deleteissue/<int:pk>/',views.Issuesdelete, name='delete'),
]